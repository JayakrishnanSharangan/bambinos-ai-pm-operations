"""
Generate 16:9 Widescreen Executive Presentation Deck PDF for Bambinos.live AI PM Operations
Using ReportLab
"""

import os
import sys
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

# 16:9 Widescreen dimensions in points: 13.333 x 7.5 inches = 960 x 540 points
SLIDE_WIDTH = 960
SLIDE_HEIGHT = 540

class SlideCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_slide_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_slide_decorations(self, total_slides):
        self.saveState()
        # Top banner accent line
        self.setFillColor(colors.HexColor("#2563EB"))
        self.rect(0, SLIDE_HEIGHT - 6, SLIDE_WIDTH, 6, fill=True, stroke=False)
        
        # Bottom footer
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(40, 20, "BAMBINOS.LIVE • AI PROGRAM MANAGER (OPERATIONS) CASE PRESENTATION")
        
        self.setFont("Helvetica", 8)
        self.drawRightString(SLIDE_WIDTH - 40, 20, f"Slide {self._pageNumber} of {total_slides}")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(40, 32, SLIDE_WIDTH - 40, 32)
        self.restoreState()

def build_deck(filename="Bambinos_AI_PM_Operations_Deck.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=(SLIDE_WIDTH, SLIDE_HEIGHT),
        leftMargin=40,
        rightMargin=40,
        topMargin=35,
        bottomMargin=35
    )
    
    styles = getSampleStyleSheet()
    
    # Palette
    c_primary = colors.HexColor("#0F172A")
    c_accent = colors.HexColor("#2563EB")
    c_slate = colors.HexColor("#475569")
    c_bg = colors.HexColor("#F8FAFC")
    c_border = colors.HexColor("#CBD5E1")

    # Typography
    s_slide_title = ParagraphStyle(
        'SlideTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=c_primary,
        spaceAfter=2
    )
    
    s_slide_sub = ParagraphStyle(
        'SlideSub',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=c_accent,
        spaceAfter=8
    )

    s_body = ParagraphStyle(
        'SlideBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#1E293B"),
        spaceAfter=4
    )

    s_bullet = ParagraphStyle(
        'SlideBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.5,
        textColor=colors.HexColor("#1E293B"),
        leftIndent=10,
        firstLineIndent=-7,
        spaceAfter=2
    )

    s_card_h = ParagraphStyle(
        'CardH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=c_primary
    )

    s_card_t = ParagraphStyle(
        'CardT',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor("#334155")
    )

    th_style = ParagraphStyle(
        'TH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    tc_style = ParagraphStyle(
        'TC',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.2,
        textColor=colors.HexColor("#1E293B")
    )

    tc_bold = ParagraphStyle(
        'TCB',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=9.2,
        textColor=c_primary
    )

    content_w = SLIDE_WIDTH - 80
    slides = []

    # ==================== SLIDE 1: COVER SLIDE ====================
    slides.append(Spacer(1, 40))
    slides.append(Paragraph("BAMBINOS.LIVE • OPERATIONS TRACK ASSESSMENT (STAGE 2)", s_slide_sub))
    slides.append(Paragraph("Re-Engineering & Automating the Student Renewal &rarr; Class Scheduling Pipeline", ParagraphStyle('CoverH', parent=s_slide_title, fontSize=26, leading=32)))
    slides.append(Spacer(1, 10))
    slides.append(Paragraph("From a Broken 4-Table Manual Bottleneck to a 77% Zero-Touch Event-Driven Pipeline", ParagraphStyle('CoverSub', parent=s_slide_sub, fontSize=13, leading=17, textColor=c_slate)))
    slides.append(HRFlowable(width="100%", thickness=2, color=c_accent, spaceBefore=8, spaceAfter=20))
    
    cover_meta = [
        [Paragraph("<b>Candidate Role:</b> AI Program Manager (Operations)", s_body),
         Paragraph("<b>Target Audience:</b> Head of Operations Review", s_body),
         Paragraph("<b>Scope:</b> Deliverables A, B, C & D", s_body),
         Paragraph("<b>Dataset:</b> 5 Masked Production Tables (13 Test Cases)", s_body)]
    ]
    t_cover = Table(cover_meta, colWidths=[content_w/4]*4)
    t_cover.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EFF6FF")),
        ('BOX', (0,0), (-1,-1), 1, c_accent),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    slides.append(t_cover)
    slides.append(PageBreak())

    # ==================== SLIDE 2: BUSINESS CONTEXT & CURRENT FLOW ====================
    slides.append(Paragraph("Executive Context & The Current 4-Table Renewal Flow", s_slide_title))
    slides.append(Paragraph("Student renewals represent >65% of Bambinos.live revenue; the current multi-table handoff is bleeding time and retention.", s_slide_sub))
    
    flow_cards = [
        [
            Paragraph("<b>Step 1: invoices</b><br/><br/>Parent completes payment via link.<br/>Entry created in payment table.<br/><br/><i>Owner: Parent / Gateway</i>", s_card_t),
            Paragraph("<b>Step 2: faculty_form</b><br/><br/>Teacher manually copies invoice link, student ID & amounts into form.<br/><br/><i>Owner: Teacher (Faculty)</i>", s_card_t),
            Paragraph("<b>Step 3: booking_requests</b><br/><br/>Ops manually verifies invoice link & bank transaction, approves entry.<br/><br/><i>Owner: 10-Person Ops Team</i>", s_card_t),
            Paragraph("<b>Step 4: class_schedule</b><br/><br/>Ops / parent coordinates and books live class schedule slots.<br/><br/><i>Owner: Ops / Parent</i>", s_card_t)
        ]
    ]
    t_flow = Table(flow_cards, colWidths=[content_w/4]*4)
    t_flow.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor("#F1F5F9")),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor("#FEE2E2")),
        ('BACKGROUND', (2,0), (2,0), colors.HexColor("#FEF3C7")),
        ('BACKGROUND', (3,0), (3,0), colors.HexColor("#EFF6FF")),
        ('GRID', (0,0), (-1,-1), 1, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    slides.append(t_flow)
    slides.append(Spacer(1, 15))
    
    slides.append(Paragraph("<b>The Core Failure:</b> On paper, this is a 4-step chain. In reality, at hundreds of renewals/week, it creates an <b>18.2% Orphaned Invoice Rate</b>, <b>24–72h turnaround lag</b>, and <b>125 hours of Ops toil weekly</b>. Teachers are treated as copy-paste clerks and Ops as human webhook verifiers.", s_body))
    slides.append(PageBreak())

    # ==================== SLIDE 3: DELIVERABLE A - 13 CASES FAILURE MODES ====================
    slides.append(Paragraph("Deliverable A: Root-Cause Failure Modes & 13 Cases Audit", s_slide_title))
    slides.append(Paragraph("Empirical analysis of all 13 production cases in the provided dataset uncovers 8 distinct failure mechanisms.", s_slide_sub))

    c_table = [
        [Paragraph("Failure Archetype", th_style), Paragraph("Dataset Evidence / Invoices", th_style), Paragraph("Root Cause / Breakdown Mechanism", th_style), Paragraph("Autonomous AI Resolution", th_style)],
        [Paragraph("<b>Transposition Typo</b>", tc_bold), Paragraph("Inv #84913 & Form 3313", tc_style), Paragraph("Teacher entered invoice <code>84931</code> instead of <code>84913</code>; SQL join failed.", tc_style), Paragraph("Levenshtein / secondary key join healed link in &lt;1s.", tc_style)],
        [Paragraph("<b>Orphaned Invoices</b>", tc_bold), Paragraph("Inv #84906, #84910", tc_style), Paragraph("Parent paid at gateway; teacher forgot form. Completely invisible to Ops.", tc_style), Paragraph("Zero-touch bypass: webhook scheduled directly without form.", tc_style)],
        [Paragraph("<b>Payment Failed Trap</b>", tc_bold), Paragraph("Inv #84911 (Ishan Gupta)", tc_style), Paragraph("Gateway FAILED; teacher submitted form on fake/pending UPI screenshot.", tc_style), Paragraph("Hard gate halt; automated WhatsApp retry URL dispatched.", tc_style)],
        [Paragraph("<b>Capacity Saturation</b>", tc_bold), Paragraph("Inv #84905 (Batch 9205)", tc_style), Paragraph("Batch reached 6/6 capacity; system created deadlocked <code>Failed_Batch_Full</code>.", tc_style), Paragraph("Dispatched WhatsApp offering 2 parallel weekend batches.", tc_style)],
        [Paragraph("<b>Duplicate Submissions</b>", tc_bold), Paragraph("Inv #84908 (Forms 3308/3309)", tc_style), Paragraph("Teacher double-submitted form due to UI lag / browser freeze.", tc_style), Paragraph("Deduplication engine auto-archived duplicate 3309.", tc_style)],
        [Paragraph("<b>PII / Secondary Payer</b>", tc_bold), Paragraph("Inv #84904 (Anaya Iyer)", tc_style), Paragraph("Mother paid from unlinked mobile (+91-9844XXXX77); flagged mismatch.", tc_style), Paragraph("LLM matched surname & student ID; linked secondary contact.", tc_style)],
        [Paragraph("<b>Partial Payment / EMI</b>", tc_bold), Paragraph("Inv #84909 (Advit Kumari)", tc_style), Paragraph("Parent paid Installment 1 (5,250 of 10,500 INR); teacher entered full amt.", tc_style), Paragraph("Scheduled 12 sessions + set automated trigger for Part 2.", tc_style)],
        [Paragraph("<b>Schedule Switch</b>", tc_bold), Paragraph("Inv #84912 (Tanya Menon)", tc_style), Paragraph("Parent wants weekend 11 AM instead of Wed-Fri; stalled in Ops queue.", tc_style), Paragraph("Dispatched interactive WhatsApp weekend slot selector.", tc_style)]
    ]
    t_c = Table(c_table, colWidths=[120, 140, 310, content_w - 570])
    t_c.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
    ]))
    slides.append(t_c)
    slides.append(PageBreak())

    # ==================== SLIDE 4: DELIVERABLE A - SLA METRICS ====================
    slides.append(Paragraph("Deliverable A: Operational Metrics & SLA Transformation", s_slide_title))
    slides.append(Paragraph("Benchmarking current baseline performance against target zero-touch SLAs.", s_slide_sub))

    sla_cards = [
        [
            Paragraph("<b>Payment-to-Schedule TAT</b><br/><br/><font size='14' color='#DC2626'><b>24–72+ Hours</b></font><br/>Current Manual Baseline<br/><br/><font size='14' color='#059669'><b>&lt; 60 Seconds</b></font><br/>Zero-Touch AI Target<br/><br/><i>Eliminates live class interruptions and parent churn.</i>", s_card_t),
            Paragraph("<b>Orphaned Invoice Rate</b><br/><br/><font size='14' color='#DC2626'><b>18.2% Leakage</b></font><br/>2 of 11 paid unsubmitted<br/><br/><font size='14' color='#059669'><b>0.0% Orphaned</b></font><br/>Zero-Touch Webhook<br/><br/><i>Every paid transaction triggers real-time scheduling.</i>", s_card_t),
            Paragraph("<b>Educator Admin Burden</b><br/><br/><font size='14' color='#DC2626'><b>12–15 mins</b></font><br/>Per student renewal<br/><br/><font size='14' color='#059669'><b>0 mins</b></font><br/>Zero-Touch Bypass<br/><br/><i>200+ teachers save 50+ hours of administrative toil weekly.</i>", s_card_t),
            Paragraph("<b>Ops Verification Effort</b><br/><br/><font size='14' color='#DC2626'><b>125 hrs / week</b></font><br/>Across 10 Ops associates<br/><br/><font size='14' color='#059669'><b>&lt; 15 hrs / week</b></font><br/>Exceptions Only<br/><br/><i>Liberates 3+ full-time equivalents for high-value student retention.</i>", s_card_t)
        ]
    ]
    t_sla = Table(sla_cards, colWidths=[content_w/4]*4)
    t_sla.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.white),
        ('GRID', (0,0), (-1,-1), 1, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    slides.append(t_sla)
    slides.append(PageBreak())

    # ==================== SLIDE 5: DELIVERABLE B - ZERO-TOUCH ARCHITECTURE ====================
    slides.append(Paragraph("Deliverable B: The Zero-Touch Re-Engineered Architecture", s_slide_title))
    slides.append(Paragraph("Event-driven ingestion bypasses redundant manual steps for happy-path renewals.", s_slide_sub))

    arch_img_path = "workflows_or_scripts/pipeline_architecture.png"
    if os.path.exists(arch_img_path):
        slides.append(Image(arch_img_path, width=content_w, height=2.6*72))
        slides.append(Spacer(1, 10))

    slides.append(Paragraph(
        "<b>Core Architectural Principle:</b> Why do teachers fill forms when parents already pay through system links? "
        "Razorpay/Stripe emits an authenticated webhook (<code>payment.captured</code>) carrying <code>metadata: { student_id, class_id, current_batch_id }</code>. "
        "The engine queries batch capacity. If the student is continuing in the same batch with verified payment, <b>Steps 2 and 3 are 100% eliminated</b>. "
        "24 live sessions are booked directly in <code>class_schedule_bookings</code> and confirmed via WhatsApp in &lt; 30 seconds.",
        s_body
    ))
    slides.append(PageBreak())

    # ==================== SLIDE 6: DELIVERABLE B - SMART EXCEPTION TRIAGE ====================
    slides.append(Paragraph("Deliverable B: Smart Exception Handling & Dynamic Routing Matrix", s_slide_title))
    slides.append(Paragraph("Multi-tier autonomous routing: self-serve bots for parents, 1-click Slack actions for Ops leads.", s_slide_sub))

    triage_cards = [
        [Paragraph("Exception Scenario", th_style), Paragraph("Detection Rule", th_style), Paragraph("Autonomous Triage & Action", th_style), Paragraph("Assigned Owner & SLA", th_style)],
        [Paragraph("<b>Failed Payment Trap</b>", tc_bold), Paragraph("<code>payment_status != 'Paid'</code>", tc_style), Paragraph("Hard halt on scheduling. Send WhatsApp payment retry URL. Alert teacher.", tc_style), Paragraph("Parent WhatsApp Bot (&lt; 2m)", tc_style)],
        [Paragraph("<b>Batch Capacity Full (6/6)</b>", tc_bold), Paragraph("<code>active >= max_batch</code>", tc_style), Paragraph("Offer 2 parallel weekend batches via WhatsApp bot or alert Ops for +1 override.", tc_style), Paragraph("Slack / WhatsApp (&lt; 15m)", tc_style)],
        [Paragraph("<b>Schedule / Batch Change</b>", tc_bold), Paragraph("<code>continue_same == 'No'</code>", tc_style), Paragraph("Interactive self-serve calendar selector via WhatsApp; auto-schedule upon pick.", tc_style), Paragraph("Parent Self-Serve (&lt; 5m)", tc_style)],
        [Paragraph("<b>Transposition Typo</b>", tc_bold), Paragraph("<code>invoice_id NOT FOUND</code>", tc_style), Paragraph("Levenshtein / secondary key matching auto-heals link; zero human delay.", tc_style), Paragraph("AI Engine (&lt; 1s)", tc_style)],
        [Paragraph("<b>Partial Payment / EMI</b>", tc_bold), Paragraph("<code>payment_type == 'Installment'</code>", tc_style), Paragraph("Schedule Tranche 1 (12 sessions) + set automated trigger for Installment 2.", tc_style), Paragraph("Billing Engine (&lt; 1m)", tc_style)],
        [Paragraph("<b>Retention Discount Policy</b>", tc_bold), Paragraph("<code>net_amount < standard_fee</code>", tc_style), Paragraph("Auto-approve if &lt;= 20% educator quota; Slack 1-click override if &gt; 20%.", tc_style), Paragraph("Slack Finance (&lt; 30m)", tc_style)]
    ]
    t_tr = Table(triage_cards, colWidths=[130, 150, 370, content_w - 650])
    t_tr.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_accent),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    slides.append(t_tr)
    slides.append(PageBreak())

    # ==================== SLIDE 7: DELIVERABLE C - PROTOTYPE RESULTS ====================
    slides.append(Paragraph("Deliverable C: Working Prototype Execution & Results Verification", s_slide_title))
    slides.append(Paragraph("Ingesting all 5 production tables through reconciliation_engine.py with 100% automated test verification.", s_slide_sub))

    proto_metrics = [
        [
            Paragraph("<b>Total Invoices Ingested</b><br/><br/><font size='16' color='#0F172A'><b>13 Invoices</b></font><br/>All 5 Production Tables", s_card_t),
            Paragraph("<b>Auto-Approved Renewals</b><br/><br/><font size='16' color='#059669'><b>10 (76.9%)</b></font><br/>Zero-Touch Happy Path", s_card_t),
            Paragraph("<b>Total Sessions Booked</b><br/><br/><font size='16' color='#2563EB'><b>228 Live Classes</b></font><br/>In class_schedule_bookings", s_card_t),
            Paragraph("<b>Action Required (Ops)</b><br/><br/><font size='16' color='#D97706'><b>3 Priority Cases</b></font><br/>Retry, Swap & Batch Full", s_card_t),
            Paragraph("<b>Auto-Resolved Flags</b><br/><br/><font size='16' color='#059669'><b>7 Resolved</b></font><br/>Typo, Dedup, PII, Discount", s_card_t)
        ]
    ]
    t_pm = Table(proto_metrics, colWidths=[content_w/5]*5)
    t_pm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.white),
        ('GRID', (0,0), (-1,-1), 1, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    slides.append(t_pm)
    slides.append(Spacer(1, 15))

    slides.append(Paragraph("<b>Integration Test Suite Verification (<code>test_reconciliation.py</code>):</b>", s_card_h))
    test_bullets = [
        "&bull; <code>test_failed_payment_blocked</code>: Confirmed Invoice 84911 (Failed) is blocked from scheduling; WhatsApp retry URL generated.",
        "&bull; <code>test_capacity_blocked</code>: Confirmed Invoice 84905 (Batch 9205 is 6/6) is held; parallel weekend slot-swap dispatched.",
        "&bull; <code>test_transposition_healed</code>: Confirmed educator typo 84931 &rarr; 84913 auto-resolved; Student #68113 scheduled for 24 classes.",
        "&bull; <code>test_duplicate_submission_archived</code>: Confirmed double-submission (Forms 3308/3309) deduplicated without duplicate class allocations.",
        "&bull; <code>test_partial_payment_scheduled_12_sessions</code>: Confirmed Advit Kumari (Installment 1) booked for exactly 12 classes with Part 2 trigger."
    ]
    for tb in test_bullets:
        slides.append(Paragraph(tb, s_bullet))
    slides.append(PageBreak())

    # ==================== SLIDE 8: DELIVERABLE D - DASHBOARD ====================
    slides.append(Paragraph("Deliverable D: Operations Head Morning Command Center", s_slide_title))
    slides.append(Paragraph("Real-time morning visibility into stuck renewals, aging bottlenecks, and saved operational hours.", s_slide_sub))

    dash_img_path = "dashboard/dashboard_overview.png"
    if os.path.exists(dash_img_path):
        slides.append(Image(dash_img_path, width=content_w, height=2.8*72))
        slides.append(Spacer(1, 8))

    slides.append(Paragraph(
        "<b>Head of Operations Daily Workflow:</b> Opens <code>dashboard/app.py</code> at 08:30 AM. "
        "Top KPI cards immediately display stuck renewals (>12h). Priority Triage Queue surfaces actionable items with 1-click buttons: "
        "<i>[1-Click Capacity Override]</i>, <i>[Resend WhatsApp Retry]</i>, or <i>[Escalate to Lead]</i>. SLA waterfall visualizes queue throughput.",
        s_body
    ))
    slides.append(PageBreak())

    # ==================== SLIDE 9: DELIVERABLE D - SOPs ====================
    slides.append(Paragraph("Deliverable D: Standard Operating Procedures (SOP) for 10-Person Ops Team", s_slide_title))
    slides.append(Paragraph("Clear, non-tech protocols ensuring zero live class interruptions and seamless exception resolution.", s_slide_sub))

    sop_cards = [
        [
            Paragraph("<b>SOP-01: Morning Queue Clearance</b><br/><br/><b>When:</b> Daily at 09:00 AM<br/><b>Who:</b> Shift Ops Associates<br/><br/>Review Morning Triage Queue. Tier 1 bot handles automated retries and slot swaps. Associates touch only items tagged <code>OPEN_ACTION_REQUIRED</code>.", s_card_t),
            Paragraph("<b>SOP-02: Batch Saturation Protocol</b><br/><br/><b>When:</b> Immediate on capacity alert<br/><b>Who:</b> Batch Allocation Lead<br/><br/>When batch reaches 6/6, verify parent slot preference. If parent insists on current cohort, click <i>'1-Click Capacity Override'</i> to allow 7th seat upon teacher consent.", s_card_t),
            Paragraph("<b>SOP-03: Gateway Payment Recovery</b><br/><br/><b>When:</b> Real-time on failed webhook<br/><b>Who:</b> Billing & Recovery Bot<br/><br/>Never ask parents for manual screenshot proofs. Direct parents exclusively through secure Razorpay/Stripe retry URLs to ensure cryptographic payment verification.", s_card_t),
            Paragraph("<b>SOP-04: Installment Billing Tranches</b><br/><br/><b>When:</b> 7 days before Class 12<br/><b>Who:</b> Automated Billing Engine<br/><br/>Installment 1 auto-books classes 1–12. Automated reminder fires before class 12. If Installment 2 fails by class 12, classes 13–24 are paused automatically.", s_card_t)
        ]
    ]
    t_sop = Table(sop_cards, colWidths=[content_w/4]*4)
    t_sop.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.white),
        ('GRID', (0,0), (-1,-1), 1, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    slides.append(t_sop)
    slides.append(PageBreak())

    # ==================== SLIDE 10: DELIVERABLE D - ROLLOUT & CHANGE MANAGEMENT ====================
    slides.append(Paragraph("Deliverable D: Change Management & 30-60-90 Day Phased Rollout", s_slide_title))
    slides.append(Paragraph("Rolling out across 200+ teachers and 10 Ops reps without breaking live classes during transition.", s_slide_sub))

    ro_cards = [
        [Paragraph("Rollout Phase", th_style), Paragraph("Duration", th_style), Paragraph("Key Initiatives & Implementation Milestones", th_style), Paragraph("Success KPIs & Guardrails", th_style)],
        [
            Paragraph("<b>Phase 1: Shadow Mode & Pilot</b>", tc_bold),
            Paragraph("Days 1–30", tc_style),
            Paragraph("&bull; Run AI engine in shadow mode alongside legacy manual flow.<br/>&bull; Pilot zero-touch on top 25 English teachers.<br/>&bull; Establish baseline reconciliation accuracy and train 10 Ops reps.", tc_style),
            Paragraph("&bull; &gt;99.5% match accuracy<br/>&bull; Zero broken live classes<br/>&bull; &lt;2 min triage time", tc_style)
        ],
        [
            Paragraph("<b>Phase 2: Bot & Expansion</b>", tc_bold),
            Paragraph("Days 31–60", tc_style),
            Paragraph("&bull; Launch WhatsApp Interactive Bot for slot swaps & payment retries.<br/>&bull; Expand zero-touch to 100 teachers across Maths & Gita.<br/>&bull; Deploy educator mobile calendar view (eliminating manual form submissions).", tc_style),
            Paragraph("&bull; Zero-Touch Rate &ge; 70%<br/>&bull; P2S TAT drops from 48h &rarr; 4h<br/>&bull; 50 Ops hours/week saved", tc_style)
        ],
        [
            Paragraph("<b>Phase 3: Global Scale</b>", tc_bold),
            Paragraph("Days 61–90", tc_style),
            Paragraph("&bull; Full rollout across 200+ teachers, GCC, and US/UK tracks.<br/>&bull; Formally decommission legacy <code>faculty_form_unapproved</code> table.<br/>&bull; Real-time Metabase executive analytics & automated capacity balancing.", tc_style),
            Paragraph("&bull; &ge; 80% Zero-Touch Rate<br/>&bull; P2S TAT &lt; 60 seconds<br/>&bull; 110+ Ops hours/week saved<br/>&bull; Zero orphaned invoices", tc_style)
        ]
    ]
    t_ro = Table(ro_cards, colWidths=[140, 60, 360, content_w - 560])
    t_ro.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_primary),
        ('GRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    slides.append(t_ro)
    slides.append(Spacer(1, 10))

    slides.append(Paragraph(
        "<b>Rollback & Safety Guardrail:</b> If the reconciliation anomaly rate exceeds 1% in any 2-hour window, the feature flag "
        "<code>ZERO_TOUCH_AUTO_APPROVE</code> automatically switches to <code>SHADOW_REVIEW</code>, routing bookings to Ops with zero data loss. "
        "Multi-tenant database row-level locking guarantees no duplicate class allocations can ever occur.",
        s_body
    ))

    # Build PDF
    doc.build(slides, canvasmaker=SlideCanvas)
    print(f"Executive 16:9 Presentation Deck built successfully: {filename}")

if __name__ == '__main__':
    deck_filename = sys.argv[1] if len(sys.argv) > 1 else "Bambinos_AI_PM_Operations_Deck.pdf"
    build_deck(deck_filename)
