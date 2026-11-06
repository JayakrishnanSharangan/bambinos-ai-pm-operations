"""
Unit and Integration Tests for Bambinos.live Reconciliation & Auto-Approval Engine
"""

import os
import unittest
import pandas as pd
from reconciliation_engine import run_reconciliation

class TestReconciliationEngine(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.data_dir = "./ops/data"
        cls.output_dir = "./results"
        cls.stats, cls.approved_df, cls.exceptions_df, cls.comms_df = run_reconciliation(
            cls.data_dir, cls.output_dir
        )
        
    def test_total_invoices_ingested(self):
        """Verify all 13 invoices were ingested."""
        self.assertEqual(self.stats['total_invoices'], 13)
        
    def test_failed_payment_blocked(self):
        """Verify Invoice 84911 (Failed status) is blocked and flagged as CRITICAL exception."""
        failed_exc = self.exceptions_df[self.exceptions_df['invoice_id'] == 84911]
        self.assertEqual(len(failed_exc), 1)
        self.assertEqual(failed_exc.iloc[0]['exception_code'], 'ERR_PAYMENT_FAILED_AT_GATEWAY')
        self.assertEqual(failed_exc.iloc[0]['severity'], 'CRITICAL')
        # Ensure student 68111 was not scheduled
        self.assertNotIn(68111, self.approved_df['student_id'].values)

    def test_capacity_blocked(self):
        """Verify Invoice 84905 (Batch 9205 is 6/6 full) is blocked from auto-scheduling."""
        cap_exc = self.exceptions_df[self.exceptions_df['invoice_id'] == 84905]
        self.assertEqual(len(cap_exc), 1)
        self.assertEqual(cap_exc.iloc[0]['exception_code'], 'ERR_BATCH_CAPACITY_FULL')
        self.assertNotIn(68105, self.approved_df['student_id'].values)

    def test_transposition_healed(self):
        """Verify Invoice 84913 / Form 3313 transposition (84931 -> 84913) was healed."""
        typo_exc = self.exceptions_df[self.exceptions_df['exception_code'] == 'WARN_TRANSPOSITION_TYPO_HEALED']
        self.assertEqual(len(typo_exc), 1)
        self.assertEqual(typo_exc.iloc[0]['invoice_id'], 84913)
        # Verify student 68113 was scheduled
        self.assertIn(68113, self.approved_df['student_id'].values)

    def test_duplicate_submission_archived(self):
        """Verify educator double submission for student 68108 was deduplicated."""
        dup_exc = self.exceptions_df[self.exceptions_df['exception_code'] == 'WARN_DUPLICATE_SUBMISSION_ARCHIVED']
        self.assertEqual(len(dup_exc), 1)
        self.assertEqual(dup_exc.iloc[0]['student_id'], 68108)

    def test_partial_payment_scheduled_12_sessions(self):
        """Verify student 68109 (Installment 1 of 2) is scheduled for exactly 12 sessions."""
        st_sched = self.approved_df[self.approved_df['student_id'] == 68109]
        self.assertEqual(len(st_sched), 12)

    def test_orphaned_invoices_bypassed_and_scheduled(self):
        """Verify paid invoices with missing teacher forms (84906, 84910) are scheduled via zero-touch."""
        self.assertIn(68106, self.approved_df['student_id'].values)
        self.assertIn(68110, self.approved_df['student_id'].values)

    def test_communications_drafted(self):
        """Verify communications were drafted for parents, educators, and ops."""
        recipients = set(self.comms_df['recipient_type'].unique())
        self.assertIn('Parent', recipients)
        self.assertIn('Educator', recipients)
        self.assertIn('Ops_Team', recipients)
        self.assertIn('Ops_Lead', recipients)

if __name__ == '__main__':
    unittest.main()

