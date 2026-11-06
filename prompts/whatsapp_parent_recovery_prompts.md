# WhatsApp Parent Recovery & Self-Serve Interaction Prompts

**Target Audience:** Parents across India, GCC (UAE/Saudi), and US/UK  
**Tone:** Empathetic, polite, clear, urgent yet non-intrusive, parent-centric  
**Channel:** WhatsApp Business API (Interactive Buttons & Quick Replies)

---

## 1. Payment Failed / Gateway Rejection Template

### Dynamic Input Variables:
- `{{parent_name}}`
- `{{student_name}}`
- `{{course_name}}`
- `{{amount}}`
- `{{retry_payment_url}}`

### Prompt & Template Specification:
```markdown
Hi {{parent_name}}! 👋 Thank you for choosing to continue {{student_name}}'s learning journey in {{course_name}} with Bambinos.live!

We noticed that your recent renewal payment of INR {{amount}} did not clear at the bank payment gateway. 💳

To ensure there is zero disruption to {{student_name}}'s scheduled class this week, please tap the secure link below to retry:
👉 {{retry_payment_url}}

ℹ️ Note: If any money was debited from your account, it will automatically bounce back within 24–48 hours depending on your bank. 

Need assistance? Reply 'HELP' and our support counsellor will call you immediately.
```

---

## 2. Capacity Full — Interactive Batch Re-allocation Template

### Dynamic Input Variables:
- `{{parent_name}}`
- `{{student_name}}`
- `{{current_batch_name}}`
- `{{educator_name}}`
- `{{slot_option_1}}`
- `{{slot_option_2}}`
- `{{selection_portal_url}}`

### Prompt & Template Specification:
```markdown
Hi {{parent_name}}! 🎉 Thank you for renewing {{student_name}}'s classes with {{educator_name}}!

Due to popular demand, your current batch ({{current_batch_name}}) has reached maximum capacity (6/6 learners). To maintain our strict small-group quality standards, we cannot overload this room.

We have reserved priority seats for {{student_name}} in these parallel batches:
1️⃣ Option 1: {{slot_option_1}}
2️⃣ Option 2: {{slot_option_2}}

Please reply with "1" or "2" to instantly book your slot, or tap below to explore all available weekend timings:
👉 {{selection_portal_url}}

We look forward to seeing {{student_name}} continue shining! ⭐
```

---

## 3. Self-Serve Batch / Schedule Change Request Template

### Dynamic Input Variables:
- `{{parent_name}}`
- `{{student_name}}`
- `{{preferred_days}}`
- `{{preferred_time}}`
- `{{self_serve_calendar_url}}`

### Prompt & Template Specification:
```markdown
Hi {{parent_name}}! We received your request to move {{student_name}}'s classes to {{preferred_days}} at {{preferred_time}}. 🗓️

We have curated the matching live batches taught by our certified senior faculty. You can select your child's permanent slot in one click:

👉 Confirm Batch: {{self_serve_calendar_url}}

Once you select your time, {{student_name}}'s calendar invites and Zoom links will be updated instantly.
```

---

## 4. Installment 1 of 2 Confirmation & Milestone Notice

### Dynamic Input Variables:
- `{{parent_name}}`
- `{{student_name}}`
- `{{installment_paid}}`
- `{{installment_balance}}`
- `{{next_due_date}}`

### Prompt & Template Specification:
```markdown
Hi {{parent_name}}! 🎉 We have successfully received your Term Installment 1 of INR {{installment_paid}} for {{student_name}}!

We have scheduled 12 live classes starting this week. You can view all upcoming dates and learning materials here:
👉 https://bambinos.live/my-classes

📌 Quick Note: Installment 2 (INR {{installment_balance}}) will be scheduled for {{next_due_date}} (prior to Class 12) so {{student_name}} never misses a single lesson.
```
