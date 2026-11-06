# Slack Operations Escalation & Approval Prompts

**Target Audience:** Bambinos.live Operations Team (Head of Ops, Shift Leads, Batch Schedulers)  
**Format:** Slack Block Kit JSON / Rich Markdown Cards with Interactive Action Buttons

---

## 1. Batch Capacity Contention Alert (`#ops-capacity-alerts`)

### Prompt & Message Template:
```markdown
🚨 *CAPACITY BOTTLENECK DETECTED*
*Student:* {{student_name}} (`ID: {{student_id}}`)
*Batch:* {{batch_name}} (`ID: {{batch_id}}`) | *Category:* {{category_name}}
*Educator:* {{educator_name}} (`ID: {{educator_id}}`)
*Current Capacity:* ⚠️ *{{active_count}} / {{max_capacity}} Students (FULL)*
*Invoice:* #{{invoice_id}} (Amount Paid: INR {{net_amount}})

*Recommended Automated Actions:*
🔘 `[Option A]` Authorize Teacher Capacity Override (Set Max = 7 for this cohort)
🔘 `[Option B]` Dispatch WhatsApp Parallel Slot Offer to Parent
🔘 `[Option C]` Spin Up New Section (Educator has open slot on {{open_slot}})

_Assigned to: @batch-ops-lead | SLA Target: 30 minutes_
```

---

## 2. Retention Scholarship / Pricing Authorization (`#finance-approvals`)

### Prompt & Message Template:
```markdown
💳 *DISCOUNT VERIFICATION REQUIRED*
*Student:* {{student_name}} (`ID: {{student_id}}`)
*Educator:* {{educator_name}}
*Standard Term Fee:* INR {{standard_fee}}
*Amount Paid by Parent:* INR {{net_amount}}
*Discount Applied:* INR {{discount_amount}} (*{{discount_percentage}}%*)
*Teacher Remark:* _"{{teacher_remarks}}"_

*Validation Check:*
✅ Educator has used 2 of 5 monthly retention vouchers.
✅ Student attendance in Level 1 was 94%.

*Interactive Sign-Off:*
[🟢 1-Click Approve Scholarship & Auto-Schedule]   [🔴 Reject & Send Payment Link for Balance]
```

---

## 3. Orphaned Invoice Aging Breach Alert (`#ops-critical-alerts`)

### Prompt & Message Template:
```markdown
⏰ *SLA BREACH WARNING: STUCK INVOICE > 12 HOURS*
*Invoice:* #{{invoice_id}} | *Paid At:* {{paid_at}} (Aged: *{{hours_elapsed}} hours*)
*Parent:* {{parent_name}} ({{mobile}})
*Student:* {{student_name}} (`ID: {{student_id}}`)
*Gateway Order:* `{{gateway_order_id}}` (Status: Paid)
*State:* 🔴 ZERO-TOUCH BYPASS FAILED or MANUAL INTERVENTION REQUIRED

*Triage Summary:*
No class scheduled. Student has a live session coming up in < 24 hours.
*Immediate Action:* [Claim Ticket] | [Force Schedule Batch {{batch_id}}] | [Call Parent]
```

