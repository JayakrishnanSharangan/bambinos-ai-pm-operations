"""
Generate Clean Visual Assets for Bambinos.live Operations Case
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

os.makedirs("dashboard", exist_ok=True)
os.makedirs("workflows_or_scripts", exist_ok=True)

# 1. Dashboard Overview Image
fig, ax = plt.subplots(figsize=(14, 8), facecolor='#F8FAFC')
ax.set_facecolor('#F8FAFC')
ax.axis('off')

# Title Bar
ax.text(0.02, 0.94, "Bambinos.live -- Autonomous Operations Command Center", fontsize=18, fontweight='bold', color='#0F172A')
ax.text(0.02, 0.90, "Real-time Morning Health & Zero-Touch Renewal Pipeline | Filter: All Regions (India, GCC, US/UK)", fontsize=11, color='#64748B')

# Top KPI Metric Cards
cards = [
    ("Total Invoices", "13", "Term Renewals", "#3B82F6"),
    ("Zero-Touch Rate", "76.9%", "+68% vs Legacy Flow", "#10B981"),
    ("Stuck Invoices (>12h)", "1", "Payment Failed Trap", "#EF4444"),
    ("Ops Action Required", "3", "Capacity / Retry Queue", "#F59E0B"),
    ("Hours Saved / Run", "3.25 hrs", "Zero Human Copy-Paste", "#8B5CF6")
]

card_w = 0.175
card_gap = 0.02
start_x = 0.02

for i, (title, val, subtitle, color) in enumerate(cards):
    cx = start_x + i * (card_w + card_gap)
    rect = patches.FancyBboxPatch((cx, 0.72), card_w, 0.15, boxstyle="round,pad=0.01",
                                  facecolor='white', edgecolor='#E2E8F0', linewidth=1.5)
    ax.add_patch(rect)
    top_line = patches.Rectangle((cx, 0.86), card_w, 0.01, facecolor=color)
    ax.add_patch(top_line)
    
    ax.text(cx + 0.01, 0.82, title, fontsize=10, fontweight='bold', color='#64748B')
    ax.text(cx + 0.01, 0.76, val, fontsize=18, fontweight='bold', color='#0F172A')
    ax.text(cx + 0.01, 0.73, subtitle, fontsize=8, color=color, fontweight='bold')

# Lower Left: Priority Exception Triage Queue
rect_triage = patches.FancyBboxPatch((0.02, 0.05), 0.55, 0.63, boxstyle="round,pad=0.01",
                                     facecolor='white', edgecolor='#E2E8F0', linewidth=1.5)
ax.add_patch(rect_triage)
ax.text(0.04, 0.63, "[!] Priority Exception Triage Queue (Action Required)", fontsize=13, fontweight='bold', color='#0F172A')
ax.text(0.04, 0.60, "Dynamic escalation routing: AI self-serve WhatsApp vs Ops Lead sign-off", fontsize=9, color='#64748B')

exceptions_ui = [
    ("[CRITICAL]", "Inv #84911 | Ishan Gupta", "Payment Failed at Gateway (Fake/pending screenshot)", "Sent Parent WhatsApp Retry Link | Blocked class allocation", "#FEF2F2", "#EF4444"),
    ("[HIGH]", "Inv #84905 | Rehan Patel", "Batch 9205 Full (6/6 Seats saturated)", "Offered parallel weekend slots via WhatsApp | Ops alert", "#FFFBEB", "#F59E0B"),
    ("[MEDIUM]", "Inv #84912 | Tanya Menon", "Parent Requested Schedule Change (Sat-Sun 11 AM)", "Dispatched Interactive WhatsApp Slot Selector", "#FEFCE8", "#CA8A04"),
    ("[RESOLVED]", "Inv #84913 | Deva Mehta", "Typo Healed: Invoice ID 84931 -> 84913", "Linked student #68113 | 24 sessions auto-scheduled", "#F0FDF4", "#16A34A"),
    ("[RESOLVED]", "Inv #84908 | Simra Mathur", "Duplicate Form Deduplicated (ID 3309)", "Archived duplicate | Single 24-session booking created", "#F0FDF4", "#16A34A")
]

for idx, (badge, title, desc, action, bg_c, txt_c) in enumerate(exceptions_ui):
    ey = 0.51 - idx * 0.088
    eb = patches.FancyBboxPatch((0.04, ey), 0.51, 0.075, boxstyle="round,pad=0.005",
                                facecolor=bg_c, edgecolor='#E2E8F0', linewidth=1)
    ax.add_patch(eb)
    ax.text(0.05, ey + 0.05, badge, fontsize=8, fontweight='bold', color=txt_c)
    ax.text(0.18, ey + 0.05, title, fontsize=9, fontweight='bold', color='#1E293B')
    ax.text(0.05, ey + 0.028, desc, fontsize=8, color='#475569')
    ax.text(0.05, ey + 0.010, f"Action: {action}", fontsize=7.5, fontstyle='italic', color='#0284C7')

# Lower Right: SLA Aging Waterfall & Re-Engineered Funnel
rect_right = patches.FancyBboxPatch((0.59, 0.05), 0.39, 0.63, boxstyle="round,pad=0.01",
                                    facecolor='white', edgecolor='#E2E8F0', linewidth=1.5)
ax.add_patch(rect_right)
ax.text(0.61, 0.63, "Pipeline SLA & Turnaround Time (TTR)", fontsize=13, fontweight='bold', color='#0F172A')
ax.text(0.61, 0.58, "Legacy Flow vs. AI Re-Engineered Flow", fontsize=9, fontweight='bold', color='#64748B')

bars_y = [0.52, 0.44, 0.36, 0.28]
labels = ["Payment-to-Schedule TAT", "Teacher Admin Burden", "Orphaned Invoice Aging", "Ops Verification Effort"]
legacy_vals = ["24-72 Hours", "15 mins / student", "> 12 Hours", "100% Manual"]
zero_touch_vals = ["< 60 Seconds", "0 mins (Bypassed)", "Real-time Webhook", "Only 23% Exceptions"]

for i in range(4):
    y = bars_y[i]
    ax.text(0.61, y + 0.02, labels[i], fontsize=8.5, fontweight='bold', color='#1E293B')
    p1 = patches.FancyBboxPatch((0.61, y - 0.025), 0.17, 0.035, boxstyle="round,pad=0.003", facecolor='#FEE2E2', edgecolor='#EF4444', linewidth=0.8)
    ax.add_patch(p1)
    ax.text(0.62, y - 0.015, f"Old: {legacy_vals[i]}", fontsize=7.5, color='#B91C1C', fontweight='bold')
    
    p2 = patches.FancyBboxPatch((0.79, y - 0.025), 0.17, 0.035, boxstyle="round,pad=0.003", facecolor='#DCFCE7', edgecolor='#16A34A', linewidth=0.8)
    ax.add_patch(p2)
    ax.text(0.80, y - 0.015, f"AI: {zero_touch_vals[i]}", fontsize=7.5, color='#15803D', fontweight='bold')

ax.text(0.61, 0.21, "[*] Live Auto-Communication Dispatch Feed", fontsize=10, fontweight='bold', color='#0F172A')
ax.text(0.61, 0.16, "- WhatsApp to Suresh Iyer (Inv #84904): Schedule confirmed.", fontsize=7.5, color='#475569')
ax.text(0.61, 0.125, "- WhatsApp to Poornima Joshi (Inv #84907): 20% discount confirmed.", fontsize=7.5, color='#475569')
ax.text(0.61, 0.09, "- WhatsApp to Sneha Kumari (Inv #84909): Installment 1 confirmed.", fontsize=7.5, color='#475569')
ax.text(0.61, 0.055, "- Slack to Ms. Rhea (#84906): Zero-touch renewal auto-scheduled.", fontsize=7.5, color='#475569')

plt.tight_layout()
plt.savefig("dashboard/dashboard_overview.png", dpi=300, bbox_inches='tight')
plt.close()

# 2. Pipeline Architecture Flowchart Image
fig2, ax2 = plt.subplots(figsize=(12, 6), facecolor='white')
ax2.set_facecolor('white')
ax2.axis('off')

ax2.text(0.5, 0.93, "Bambinos.live Zero-Touch Renewal Architecture", fontsize=16, fontweight='bold', ha='center', color='#0F172A')
ax2.text(0.5, 0.88, "Event-Driven Ingestion -> Deterministic & Semantic Reconciliation -> Automated Fulfillment", fontsize=10, ha='center', color='#64748B')

nodes = [
    ("Payment Webhook", "Razorpay / Stripe\n(payment.captured)", 0.10, 0.55, "#3B82F6"),
    ("Data Master Lookup", "Active Students,\nBatches & Capacity", 0.32, 0.55, "#6366F1"),
    ("AI / Logic Engine", "Typo Healer, Dedup,\nPII & Policy Checks", 0.54, 0.55, "#8B5CF6"),
    ("Auto-Scheduler", "class_schedule_bookings\n(24 Live Sessions)", 0.76, 0.70, "#10B981"),
    ("WhatsApp Parent Bot", "Instant Confirmation\nCalendar / Zoom Link", 0.95, 0.70, "#059669"),
    ("Exception Router", "Capacity / Failed Pay\nSchedule Change Triage", 0.76, 0.35, "#F59E0B"),
    ("Ops / Parent Comms", "Slack Alerts / 1-Click\nSelf-Serve Slot Swap", 0.95, 0.35, "#D97706")
]

for name, sub, x, y, c in nodes:
    box = patches.FancyBboxPatch((x - 0.08, y - 0.08), 0.16, 0.16, boxstyle="round,pad=0.01", facecolor='white', edgecolor=c, linewidth=2)
    ax2.add_patch(box)
    header = patches.Rectangle((x - 0.08, y + 0.06), 0.16, 0.02, facecolor=c)
    ax2.add_patch(header)
    ax2.text(x, y + 0.01, name, fontsize=9, fontweight='bold', ha='center', color='#1E293B')
    ax2.text(x, y - 0.04, sub, fontsize=7.5, ha='center', color='#64748B')

# Connectors
def draw_arrow(p1, p2, txt=""):
    ax2.annotate("", xy=p2, xytext=p1, arrowprops=dict(arrowstyle="->", color="#94A3B8", lw=2, mutation_scale=15))
    if txt:
        ax2.text((p1[0]+p2[0])/2, (p1[1]+p2[1])/2 + 0.03, txt, fontsize=7.5, fontweight='bold', ha='center', color='#334155')

draw_arrow((0.18, 0.55), (0.24, 0.55))
draw_arrow((0.40, 0.55), (0.46, 0.55))
draw_arrow((0.62, 0.58), (0.68, 0.70), "Happy Path (80%)")
draw_arrow((0.62, 0.52), (0.68, 0.35), "Exceptions (20%)")
draw_arrow((0.84, 0.70), (0.87, 0.70))
draw_arrow((0.84, 0.35), (0.87, 0.35))

plt.tight_layout()
plt.savefig("workflows_or_scripts/pipeline_architecture.png", dpi=300, bbox_inches='tight')
plt.close()

print("Assets generated successfully: dashboard/dashboard_overview.png and workflows_or_scripts/pipeline_architecture.png")
