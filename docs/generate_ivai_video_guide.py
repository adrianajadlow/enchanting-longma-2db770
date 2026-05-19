"""Generate a one-pager PDF guide explaining IVAI video & content strategy."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
    HRFlowable,
    ListFlowable,
    ListItem,
)

OUTPUT = "ivai-video-content-guide.pdf"

# Brand palette (matches IVAI/JT salon site)
INK = colors.HexColor("#1a1a1a")
CHARCOAL = colors.HexColor("#2b2b2b")
MUTED = colors.HexColor("#6b6b6b")
GREEN = colors.HexColor("#3f5a3a")
GREEN_PALE = colors.HexColor("#e8efe3")
BEIGE = colors.HexColor("#f5f1ea")
BEIGE2 = colors.HexColor("#e8dfd2")
ACCENT = colors.HexColor("#b08a4a")


def build_styles():
    styles = getSampleStyleSheet()
    base = "Helvetica"
    return {
        "eyebrow": ParagraphStyle(
            "eyebrow", parent=styles["Normal"], fontName=base + "-Bold",
            fontSize=8, textColor=ACCENT, leading=11, spaceAfter=4,
            tracking=1,
        ),
        "title": ParagraphStyle(
            "title", parent=styles["Title"], fontName="Times-Italic",
            fontSize=30, textColor=INK, leading=34, spaceAfter=4,
            alignment=0,
        ),
        "subtitle": ParagraphStyle(
            "subtitle", parent=styles["Normal"], fontName=base,
            fontSize=11, textColor=MUTED, leading=15, spaceAfter=14,
        ),
        "h2": ParagraphStyle(
            "h2", parent=styles["Heading2"], fontName=base + "-Bold",
            fontSize=13, textColor=GREEN, leading=16, spaceBefore=14,
            spaceAfter=6,
        ),
        "h3": ParagraphStyle(
            "h3", parent=styles["Heading3"], fontName=base + "-Bold",
            fontSize=10, textColor=INK, leading=13, spaceBefore=8,
            spaceAfter=3,
        ),
        "body": ParagraphStyle(
            "body", parent=styles["Normal"], fontName=base,
            fontSize=9.5, textColor=CHARCOAL, leading=14, spaceAfter=6,
        ),
        "bullet": ParagraphStyle(
            "bullet", parent=styles["Normal"], fontName=base,
            fontSize=9.5, textColor=CHARCOAL, leading=13.5,
        ),
        "callout": ParagraphStyle(
            "callout", parent=styles["Normal"], fontName="Times-Italic",
            fontSize=10.5, textColor=GREEN, leading=15, alignment=0,
        ),
        "stat_num": ParagraphStyle(
            "stat_num", parent=styles["Normal"], fontName="Times-Roman",
            fontSize=24, textColor=GREEN, leading=26, alignment=1,
        ),
        "stat_label": ParagraphStyle(
            "stat_label", parent=styles["Normal"], fontName=base,
            fontSize=7.5, textColor=MUTED, leading=10, alignment=1,
            spaceBefore=2,
        ),
        "footer": ParagraphStyle(
            "footer", parent=styles["Normal"], fontName=base,
            fontSize=7.5, textColor=MUTED, leading=10, alignment=1,
        ),
        "kicker": ParagraphStyle(
            "kicker", parent=styles["Normal"], fontName=base + "-Bold",
            fontSize=9, textColor=INK, leading=12, spaceAfter=2,
        ),
    }


def header_footer(canvas, doc):
    canvas.saveState()
    # Top brand bar
    canvas.setFillColor(INK)
    canvas.rect(0, LETTER[1] - 0.45 * inch, LETTER[0], 0.45 * inch, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 9)
    canvas.drawString(0.6 * inch, LETTER[1] - 0.28 * inch, "IVAI  ·  CONTENT & VIDEO BRIEF")
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(BEIGE2)
    canvas.drawRightString(LETTER[0] - 0.6 * inch, LETTER[1] - 0.28 * inch,
                           "Prepared for Leadership Review")

    # Bottom rule + page number
    canvas.setStrokeColor(BEIGE2)
    canvas.setLineWidth(0.5)
    canvas.line(0.6 * inch, 0.55 * inch, LETTER[0] - 0.6 * inch, 0.55 * inch)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawString(0.6 * inch, 0.4 * inch,
                      "IVAI  ·  Internal Memo  ·  Video Production & Content Strategy")
    canvas.drawRightString(LETTER[0] - 0.6 * inch, 0.4 * inch,
                           f"Page {doc.page}")
    canvas.restoreState()


def stat_box(num, label, S):
    inner = Table(
        [[Paragraph(num, S["stat_num"])], [Paragraph(label, S["stat_label"])]],
        colWidths=[1.6 * inch],
    )
    inner.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), GREEN_PALE),
        ("BOX", (0, 0), (-1, -1), 0, colors.transparent),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    return inner


def callout_box(text, S):
    p = Paragraph(text, S["callout"])
    t = Table([[p]], colWidths=[6.9 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BEIGE),
        ("LINEBEFORE", (0, 0), (0, -1), 2, ACCENT),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ]))
    return t


def bullets(items, S):
    flows = [
        ListItem(Paragraph(t, S["bullet"]), leftIndent=12, value="•")
        for t in items
    ]
    return ListFlowable(
        flows, bulletType="bullet", bulletChar="•",
        bulletFontName="Helvetica-Bold", bulletColor=GREEN,
        leftIndent=14, bulletFontSize=9,
    )


def build():
    doc = BaseDocTemplate(
        OUTPUT, pagesize=LETTER,
        leftMargin=0.6 * inch, rightMargin=0.6 * inch,
        topMargin=0.7 * inch, bottomMargin=0.7 * inch,
        title="IVAI — Video & Content Strategy Brief",
        author="IVAI Content Team",
    )
    frame = Frame(
        doc.leftMargin, doc.bottomMargin,
        doc.width, doc.height - 0.2 * inch,
        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        showBoundary=0,
    )
    doc.addPageTemplates([
        PageTemplate(id="main", frames=[frame], onPage=header_footer)
    ])

    S = build_styles()
    story = []

    # --- Title block ---
    story.append(Paragraph("MEMO  ·  CONTENT STRATEGY", S["eyebrow"]))
    story.append(Paragraph("Why video is IVAI's<br/><i>fastest</i> growth lever.",
                           S["title"]))
    story.append(Paragraph(
        "A short brief on how we are creating videos and content for IVAI, "
        "why it matters right now, and what the new 3-minute video workflow "
        "unlocks for the brand.",
        S["subtitle"],
    ))
    story.append(HRFlowable(width="100%", thickness=0.75, color=BEIGE2,
                             spaceBefore=2, spaceAfter=10))

    # --- Stats row ---
    stats = Table(
        [[
            stat_box("3 min", "Average production time per spot", S),
            stat_box("4×", "Active IVAI video assets in rotation", S),
            stat_box("60s", "Hero spot length for paid social", S),
            stat_box("24/7", "Always-on content engine", S),
        ]],
        colWidths=[1.7 * inch] * 4,
    )
    stats.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(stats)
    story.append(Spacer(1, 12))

    # --- Section: Why this matters ---
    story.append(Paragraph("Why this matters for IVAI", S["h2"]))
    story.append(Paragraph(
        "Short-form video is the single highest-leverage content format on "
        "every channel IVAI cares about — Instagram, TikTok, YouTube Shorts, "
        "and paid social. Video drives 3–5× the engagement of static posts, "
        "shortens the path from awareness to booking, and gives the brand a "
        "consistent on-screen identity that text and photography cannot match.",
        S["body"],
    ))
    story.append(Paragraph(
        "For IVAI specifically, video lets us <b>show the transformation</b> "
        "— the cut, the color, the room, the people — in a way that converts "
        "scrollers into clients. It is also reusable: one shoot fuels weeks "
        "of organic posts, paid ads, website hero loops, and email assets.",
        S["body"],
    ))

    # --- Callout: the 3-minute aspect ---
    story.append(Spacer(1, 4))
    story.append(callout_box(
        "“The 3-minute video creation workflow means a finished, on-brand "
        "spot in the time it used to take to write a caption — turning IVAI "
        "into a daily publisher instead of a quarterly one.”",
        S,
    ))

    # --- Section: The 3-minute workflow ---
    story.append(Paragraph("The 3-minute video creation workflow", S["h2"]))
    story.append(Paragraph(
        "We've built a pipeline that takes a raw idea to a published, "
        "on-brand IVAI video in roughly three minutes. This is the unlock — "
        "speed at brand quality.",
        S["body"],
    ))

    workflow = Table(
        [[
            Paragraph("<b>0:00 → 0:30</b><br/>"
                      "<font color='#6b6b6b' size='8'>Brief & prompt</font>",
                      S["bullet"]),
            Paragraph("<b>0:30 → 1:30</b><br/>"
                      "<font color='#6b6b6b' size='8'>AI generation + b-roll</font>",
                      S["bullet"]),
            Paragraph("<b>1:30 → 2:30</b><br/>"
                      "<font color='#6b6b6b' size='8'>Brand polish & captions</font>",
                      S["bullet"]),
            Paragraph("<b>2:30 → 3:00</b><br/>"
                      "<font color='#6b6b6b' size='8'>Review &amp; publish</font>",
                      S["bullet"]),
        ]],
        colWidths=[1.7 * inch] * 4,
    )
    workflow.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ("BOX", (0, 0), (-1, -1), 0.5, BEIGE2),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, BEIGE2),
        ("LINEABOVE", (0, 0), (-1, 0), 2, GREEN),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(workflow)
    story.append(Spacer(1, 10))

    story.append(Paragraph("What this changes for the business", S["h3"]))
    story.append(bullets([
        "<b>Volume.</b> We can ship a fresh spot every day rather than once "
        "a quarter — keeping IVAI top-of-feed and top-of-mind.",
        "<b>Cost.</b> The marginal cost of an additional video drops to "
        "near zero, so we can A/B test creative instead of betting on one cut.",
        "<b>Responsiveness.</b> Trends, promotions, and seasonal moments "
        "can be turned into branded content the same day they appear.",
        "<b>Brand consistency.</b> Every spot is generated against the same "
        "IVAI look — type, palette, pacing — so the feed always reads as one brand.",
    ], S))

    # --- Section: What we're producing ---
    story.append(Paragraph("What we're producing for IVAI", S["h2"]))

    catalog = Table(
        [
            [Paragraph("<b>Asset</b>", S["kicker"]),
             Paragraph("<b>Length</b>", S["kicker"]),
             Paragraph("<b>Use case</b>", S["kicker"])],
            [Paragraph("IVAI Commercial (hero)", S["bullet"]),
             Paragraph("30–45s", S["bullet"]),
             Paragraph("Website hero, paid social top-funnel", S["bullet"])],
            [Paragraph("IVAI Spot 60s", S["bullet"]),
             Paragraph("60s", S["bullet"]),
             Paragraph("YouTube pre-roll, Meta &amp; TikTok ads", S["bullet"])],
            [Paragraph("IVAI Evolve", S["bullet"]),
             Paragraph("20–30s", S["bullet"]),
             Paragraph("Brand story / about-page loop", S["bullet"])],
            [Paragraph("IVAI No-Show", S["bullet"]),
             Paragraph("15–20s", S["bullet"]),
             Paragraph("Retention &amp; booking-policy reminder", S["bullet"])],
        ],
        colWidths=[2.4 * inch, 1.0 * inch, 3.5 * inch],
    )
    catalog.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), GREEN_PALE),
        ("TEXTCOLOR", (0, 0), (-1, 0), GREEN),
        ("LINEBELOW", (0, 0), (-1, 0), 1, GREEN),
        ("LINEBELOW", (0, 1), (-1, -2), 0.25, BEIGE2),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(catalog)
    story.append(Spacer(1, 10))

    # --- The ask ---
    story.append(Paragraph("The recommendation", S["h2"]))
    story.append(Paragraph(
        "Lean in. The 3-minute pipeline is already producing the four "
        "active IVAI spots in rotation today. With sign-off, we'll scale "
        "to a weekly publishing cadence across IG, TikTok, and YouTube — "
        "and start running paid creative tests against the existing hero "
        "spot to find IVAI's highest-converting format.",
        S["body"],
    ))
    story.append(Paragraph("Next steps", S["h3"]))
    story.append(bullets([
        "Approve weekly publishing cadence (4–6 spots per month).",
        "Greenlight a small paid-social test budget against the 60s spot.",
        "Confirm brand guardrails so the team can ship without per-asset review.",
    ], S))

    doc.build(story)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    build()
