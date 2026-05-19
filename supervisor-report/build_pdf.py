"""Generate the IVAI AI Video Creation Stack Recommendation Report as a branded PDF."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

IVAI_BLUE = colors.HexColor("#0057A0")
IVAI_GREEN = colors.HexColor("#00A676")
LIGHT_GRAY = colors.HexColor("#F4F6F8")
DARK_TEXT = colors.HexColor("#1A1A1A")
MUTED_TEXT = colors.HexColor("#555555")

OUTPUT_PATH = "IVAI_AI_Video_Stack_Recommendation.pdf"


def _draw_page_chrome(canvas, doc):
    canvas.saveState()
    width, height = LETTER

    # Top accent bar (blue/green split)
    canvas.setFillColor(IVAI_BLUE)
    canvas.rect(0, height - 0.35 * inch, width * 0.55, 0.35 * inch, stroke=0, fill=1)
    canvas.setFillColor(IVAI_GREEN)
    canvas.rect(width * 0.55, height - 0.35 * inch, width * 0.45, 0.35 * inch, stroke=0, fill=1)

    # Header text inside accent bar
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 10)
    canvas.drawString(0.6 * inch, height - 0.22 * inch, "INTELLIGENT VOICE AI")
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(
        width - 0.6 * inch,
        height - 0.22 * inch,
        "AI Video Creation Stack Recommendation",
    )

    # Footer
    canvas.setStrokeColor(IVAI_BLUE)
    canvas.setLineWidth(0.75)
    canvas.line(0.6 * inch, 0.55 * inch, width - 0.6 * inch, 0.55 * inch)

    canvas.setFillColor(MUTED_TEXT)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(0.6 * inch, 0.38 * inch, "Prepared by Adriana Jadlow  |  May 2026")
    canvas.drawRightString(width - 0.6 * inch, 0.38 * inch, f"Page {doc.page}")

    canvas.restoreState()


def _draw_cover(canvas, doc):
    canvas.saveState()
    width, height = LETTER

    # Full-bleed blue header block
    canvas.setFillColor(IVAI_BLUE)
    canvas.rect(0, height - 3.2 * inch, width, 3.2 * inch, stroke=0, fill=1)

    # Green accent stripe
    canvas.setFillColor(IVAI_GREEN)
    canvas.rect(0, height - 3.45 * inch, width, 0.25 * inch, stroke=0, fill=1)

    # Logo placeholder badge (top-left)
    canvas.setFillColor(colors.white)
    canvas.setStrokeColor(colors.white)
    canvas.setLineWidth(1.5)
    canvas.roundRect(0.6 * inch, height - 1.3 * inch, 1.1 * inch, 0.7 * inch, 6, stroke=1, fill=0)
    canvas.setFont("Helvetica-Bold", 14)
    canvas.drawCentredString(1.15 * inch, height - 0.97 * inch, "IVAI")

    # Cover title
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 30)
    canvas.drawString(0.6 * inch, height - 2.0 * inch, "AI Video Creation Stack")
    canvas.setFont("Helvetica-Bold", 22)
    canvas.drawString(0.6 * inch, height - 2.45 * inch, "Recommendation Report")

    canvas.setFont("Helvetica", 12)
    canvas.drawString(0.6 * inch, height - 2.85 * inch, "Intelligent Voice AI  |  Marketing Strategy Brief")

    # Recipient / preparer block
    canvas.setFillColor(LIGHT_GRAY)
    canvas.rect(0.6 * inch, height - 5.6 * inch, width - 1.2 * inch, 1.6 * inch, stroke=0, fill=1)

    canvas.setFillColor(IVAI_BLUE)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.drawString(0.85 * inch, height - 4.05 * inch, "PREPARED FOR")
    canvas.setFillColor(DARK_TEXT)
    canvas.setFont("Helvetica", 12)
    canvas.drawString(0.85 * inch, height - 4.3 * inch, "Shannon Diem, Founder & CEO")
    canvas.drawString(0.85 * inch, height - 4.5 * inch, "Intelligent Voice AI")

    canvas.setFillColor(IVAI_GREEN)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.drawString(0.85 * inch, height - 4.9 * inch, "PREPARED BY")
    canvas.setFillColor(DARK_TEXT)
    canvas.setFont("Helvetica", 12)
    canvas.drawString(0.85 * inch, height - 5.15 * inch, "Adriana Jadlow")
    canvas.drawString(0.85 * inch, height - 5.35 * inch, "Marketing & Social Media Strategist")

    # Date block
    canvas.setFillColor(IVAI_BLUE)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.drawString(0.6 * inch, 1.6 * inch, "DATE")
    canvas.setFillColor(DARK_TEXT)
    canvas.setFont("Helvetica", 12)
    canvas.drawString(0.6 * inch, 1.35 * inch, "May 2026")

    # Footer bar
    canvas.setFillColor(IVAI_BLUE)
    canvas.rect(0, 0, width, 0.45 * inch, stroke=0, fill=1)
    canvas.setFillColor(IVAI_GREEN)
    canvas.rect(0, 0.45 * inch, width, 0.08 * inch, stroke=0, fill=1)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 9)
    canvas.drawCentredString(width / 2, 0.18 * inch, "Confidential  |  Internal Strategy Document")

    canvas.restoreState()


def _make_styles():
    base = getSampleStyleSheet()
    styles = {
        "body": ParagraphStyle(
            "body",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=15,
            textColor=DARK_TEXT,
            spaceAfter=8,
            alignment=TA_LEFT,
        ),
        "h1": ParagraphStyle(
            "h1",
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=24,
            textColor=IVAI_BLUE,
            spaceBefore=6,
            spaceAfter=10,
        ),
        "h2": ParagraphStyle(
            "h2",
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            textColor=IVAI_GREEN,
            spaceBefore=12,
            spaceAfter=6,
        ),
        "h3": ParagraphStyle(
            "h3",
            fontName="Helvetica-Bold",
            fontSize=11.5,
            leading=15,
            textColor=IVAI_BLUE,
            spaceBefore=8,
            spaceAfter=4,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            fontName="Helvetica",
            fontSize=10.5,
            leading=14,
            leftIndent=14,
            bulletIndent=2,
            textColor=DARK_TEXT,
            spaceAfter=2,
        ),
        "check": ParagraphStyle(
            "check",
            fontName="Helvetica",
            fontSize=10.5,
            leading=15,
            leftIndent=14,
            textColor=DARK_TEXT,
            spaceAfter=2,
        ),
        "callout": ParagraphStyle(
            "callout",
            fontName="Helvetica-Oblique",
            fontSize=11,
            leading=15,
            textColor=IVAI_BLUE,
            leftIndent=10,
            rightIndent=10,
            spaceBefore=6,
            spaceAfter=10,
        ),
        "small": ParagraphStyle(
            "small",
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            textColor=MUTED_TEXT,
        ),
        "section_label": ParagraphStyle(
            "section_label",
            fontName="Helvetica-Bold",
            fontSize=9,
            leading=12,
            textColor=colors.white,
            alignment=TA_LEFT,
        ),
    }
    return styles


def _section_banner(text, color, styles):
    tbl = Table(
        [[Paragraph(text.upper(), styles["section_label"])]],
        colWidths=[7.0 * inch],
    )
    tbl.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), color),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return tbl


def _styled_table(data, col_widths, header_color=IVAI_BLUE, highlight_row=None):
    tbl = Table(data, colWidths=col_widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), header_color),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 9.5),
        ("TEXTCOLOR", (0, 1), (-1, -1), DARK_TEXT),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GRAY]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#D6DCE2")),
    ]
    if highlight_row is not None:
        style.append(("BACKGROUND", (0, highlight_row), (-1, highlight_row), colors.HexColor("#E6F4EC")))
        style.append(("FONTNAME", (0, highlight_row), (-1, highlight_row), "Helvetica-Bold"))
    tbl.setStyle(TableStyle(style))
    return tbl


def build():
    doc = BaseDocTemplate(
        OUTPUT_PATH,
        pagesize=LETTER,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
        topMargin=0.7 * inch,
        bottomMargin=0.7 * inch,
        title="IVAI AI Video Creation Stack Recommendation",
        author="Adriana Jadlow",
    )

    frame_cover = Frame(0, 0, *LETTER, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="cover")
    frame_body = Frame(
        0.6 * inch,
        0.7 * inch,
        LETTER[0] - 1.2 * inch,
        LETTER[1] - 1.4 * inch,
        id="body",
    )

    doc.addPageTemplates(
        [
            PageTemplate(id="Cover", frames=frame_cover, onPage=_draw_cover),
            PageTemplate(id="Body", frames=frame_body, onPage=_draw_page_chrome),
        ]
    )

    s = _make_styles()
    story = []

    # === Cover page (drawn entirely on canvas) ===
    story.append(Spacer(1, 0.1 * inch))
    story.append(PageBreak())

    # Switch to body template after cover
    from reportlab.platypus import NextPageTemplate
    # The first PageBreak above ends cover; ensure body template kicks in.
    # We re-issue NextPageTemplate to be safe.
    story.insert(0, NextPageTemplate("Body"))

    # === Section 1: Executive Summary ===
    story.append(_section_banner("1. Executive Summary", IVAI_BLUE, s))
    story.append(Spacer(1, 0.15 * inch))
    story.append(
        Paragraph(
            "This report outlines the best, easiest, and highest-quality AI video creation stack "
            "for Intelligent Voice AI (IVAI), designed to support Instagram Reels, TikTok videos, "
            "YouTube Shorts, YouTube videos up to three minutes, cinematic commercial-grade visuals, "
            "avatar-driven content using HeyGen, an ElevenLabs cloned voice, and full developer "
            "compatibility with VS Code, GitHub, Node.js, Python, and PowerShell.",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "After evaluating all leading platforms, the recommended stack is:",
            s["body"],
        )
    )
    story.append(
        Paragraph(
            "<b>HeyGen</b> (core editor) + <b>Runway Gen-4.5</b> (cinematic engine) + "
            "<b>ElevenLabs</b> (voice) + optional <b>Sora 2</b> (premium realism).",
            s["callout"],
        )
    )
    story.append(
        Paragraph(
            "This combination delivers the highest cinematic quality, the easiest workflow, and full "
            "compatibility with IVAI's existing assets and future marketing goals.",
            s["body"],
        )
    )

    # === Section 2: Why This Stack ===
    story.append(Spacer(1, 0.15 * inch))
    story.append(_section_banner("2. Why This Stack Is the Best Choice for IVAI", IVAI_GREEN, s))
    story.append(Spacer(1, 0.15 * inch))
    story.append(
        Paragraph(
            "This stack was selected because it meets every requirement IVAI has:",
            s["body"],
        )
    )
    for line in [
        "Supports reels, shorts, and 3-minute videos",
        "Highest cinematic quality available in 2026",
        "Works with your existing HeyGen avatars",
        "Works with your ElevenLabs cloned voice",
        "Compatible with your developer tools",
        "Commercial-safe licensing",
        "Easy to use, fast to produce, and scalable",
    ]:
        story.append(Paragraph(f'<font color="#00A676"><b>&#10003;</b></font>&nbsp;&nbsp;{line}', s["check"]))
    story.append(Spacer(1, 0.08 * inch))
    story.append(
        Paragraph(
            "This is the same stack used by top agencies, enterprise teams, and commercial creators.",
            s["body"],
        )
    )

    story.append(PageBreak())

    # === Section 3: Platform Evaluations ===
    story.append(_section_banner("3. Platform Evaluations & Pricing", IVAI_BLUE, s))
    story.append(Spacer(1, 0.2 * inch))

    # 3.1 HeyGen
    story.append(Paragraph("3.1 HeyGen — Core Editor & Avatar Platform", s["h2"]))
    story.append(Paragraph("Purpose", s["h3"]))
    story.append(
        Paragraph(
            "HeyGen is the central hub for assembling all videos — reels, shorts, and 3-minute "
            "YouTube videos. It is the only platform that integrates perfectly with your existing "
            "IVAI avatars and ElevenLabs voice.",
            s["body"],
        )
    )
    story.append(Paragraph("Key Features", s["h3"]))
    for f in [
        "Hyper-realistic avatars",
        "Multi-scene editor (supports 3+ minutes)",
        "Imports previous HeyGen videos",
        "Perfect ElevenLabs lip-sync",
        "Commercial licensing",
        "API for automation (Node.js, Python, PowerShell compatible)",
    ]:
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{f}", s["bullet"]))
    story.append(Paragraph("Why It Matters for IVAI", s["h3"]))
    story.append(
        Paragraph(
            "HeyGen is where your avatar, voice, and cinematic clips come together. It is the easiest "
            "and most stable platform for assembling polished, professional videos.",
            s["body"],
        )
    )
    story.append(Paragraph("Pricing (2026)", s["h3"]))
    story.append(
        _styled_table(
            [
                ["Plan", "Price", "Includes"],
                ["Creator", "~$29 / mo", "Basic avatars, limited exports"],
                ["Business (Recommended)", "~$89 / mo", "HD exports, brand kits, commercial rights"],
                ["Enterprise", "Custom", "API access, unlimited avatars, team seats"],
            ],
            col_widths=[1.9 * inch, 1.3 * inch, 3.8 * inch],
            header_color=IVAI_BLUE,
            highlight_row=2,
        )
    )
    story.append(Spacer(1, 0.05 * inch))
    story.append(Paragraph("<b>Recommended for IVAI:</b> Business or Enterprise.", s["body"]))

    # 3.2 Runway
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("3.2 Runway Gen-4.5 — Cinematic Motion Engine", s["h2"]))
    story.append(Paragraph("Purpose", s["h3"]))
    story.append(
        Paragraph(
            "Runway Gen-4.5 generates the cinematic motion that makes your videos look like professional commercials.",
            s["body"],
        )
    )
    story.append(Paragraph("Key Features", s["h3"]))
    for f in [
        "Industry-leading camera motion",
        "Realistic lighting and physics",
        "Perfect for intros, transitions, and commercial visuals",
        "API support (Node.js, Python)",
    ]:
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{f}", s["bullet"]))
    story.append(Paragraph("Why It Matters for IVAI", s["h3"]))
    story.append(
        Paragraph(
            "HeyGen avatars are strong, but they don't generate cinematic B-roll. Runway fills that "
            "gap with dynamic camera shots, scene transitions, high-end visuals, and background footage. "
            "These clips elevate your videos from \"AI-generated\" to commercial-grade.",
            s["body"],
        )
    )
    story.append(Paragraph("Pricing (2026)", s["h3"]))
    story.append(
        _styled_table(
            [
                ["Plan", "Price", "Includes"],
                ["Standard", "~$15 / mo", "Limited credits"],
                ["Pro (Recommended)", "~$35 / mo", "More credits, 4K exports"],
                ["Unlimited", "~$95 / mo", "High-volume generation"],
            ],
            col_widths=[1.9 * inch, 1.3 * inch, 3.8 * inch],
            header_color=IVAI_GREEN,
            highlight_row=2,
        )
    )
    story.append(Spacer(1, 0.05 * inch))
    story.append(Paragraph("<b>Recommended for IVAI:</b> Pro or Unlimited.", s["body"]))

    story.append(PageBreak())

    # 3.3 ElevenLabs
    story.append(Paragraph("3.3 ElevenLabs — Voice Cloning & Audio Layer", s["h2"]))
    story.append(Paragraph("Purpose", s["h3"]))
    story.append(
        Paragraph(
            "ElevenLabs provides the voice that drives your avatar videos and reels.",
            s["body"],
        )
    )
    story.append(Paragraph("Key Features", s["h3"]))
    for f in [
        "Perfect lip-sync with HeyGen",
        "Emotional modulation",
        "Multilingual support",
        "API for automation (Node.js, Python, PowerShell)",
    ]:
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{f}", s["bullet"]))
    story.append(Paragraph("Why It Matters for IVAI", s["h3"]))
    story.append(
        Paragraph(
            "Your cloned voice ensures brand consistency, a professional tone, natural delivery, and fast production.",
            s["body"],
        )
    )
    story.append(Paragraph("Pricing (2026)", s["h3"]))
    story.append(
        _styled_table(
            [
                ["Plan", "Price", "Includes"],
                ["Starter", "~$5 / mo", "Basic generation"],
                ["Creator (Recommended)", "~$22 / mo", "Voice cloning, more credits"],
                ["Pro", "~$99 / mo", "High-volume, commercial rights"],
            ],
            col_widths=[1.9 * inch, 1.3 * inch, 3.8 * inch],
            header_color=IVAI_BLUE,
            highlight_row=2,
        )
    )
    story.append(Spacer(1, 0.05 * inch))
    story.append(Paragraph("<b>Recommended for IVAI:</b> Creator or Pro.", s["body"]))

    # 3.4 Sora 2
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("3.4 Sora 2 — Premium Cinematic Engine (Optional)", s["h2"]))
    story.append(Paragraph("Purpose", s["h3"]))
    story.append(
        Paragraph(
            "Sora 2 is the highest-quality cinematic engine available, producing Hollywood-level realism.",
            s["body"],
        )
    )
    story.append(Paragraph("Key Features", s["h3"]))
    for f in [
        "Physics-accurate motion",
        "Realistic lighting, reflections, and materials",
        "Long-form generation",
        "Director-level camera control",
    ]:
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{f}", s["bullet"]))
    story.append(Paragraph("Why It Matters for IVAI", s["h3"]))
    story.append(
        Paragraph(
            "If you want premium commercial visuals, Sora 2 is unmatched. It is optional, but extremely powerful.",
            s["body"],
        )
    )
    story.append(Paragraph("Pricing", s["h3"]))
    story.append(
        _styled_table(
            [
                ["Plan", "Availability", "Notes"],
                ["Enterprise only", "Invite-only", "Pricing varies"],
            ],
            col_widths=[1.9 * inch, 1.5 * inch, 3.6 * inch],
            header_color=IVAI_GREEN,
        )
    )

    story.append(PageBreak())

    # === Section 4: How the Stack Works Together ===
    story.append(_section_banner("4. How the Entire Stack Works Together", IVAI_BLUE, s))
    story.append(Spacer(1, 0.2 * inch))
    story.append(
        Paragraph(
            "This section explains exactly how the platforms combine to produce reels, shorts, "
            "and 3-minute videos.",
            s["body"],
        )
    )

    story.append(Paragraph("Step 1 — Cinematic Clip Generation (Runway Gen-4.5 / Sora 2)", s["h3"]))
    for f in [
        "3-10 second cinematic B-roll",
        "Dynamic camera shots",
        "Scene openers",
        "Transitions",
        "Background visuals",
    ]:
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{f}", s["bullet"]))
    story.append(
        Paragraph(
            "These clips become the cinematic backbone of your videos.",
            s["body"],
        )
    )

    story.append(Paragraph("Step 2 — Voice Generation (ElevenLabs)", s["h3"]))
    for f in ["Hooks", "Narration", "Explanations", "Calls-to-action"]:
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{f}", s["bullet"]))
    story.append(
        Paragraph(
            "Your cloned voice ensures consistency, emotional tone, and perfect lip-sync inside HeyGen.",
            s["body"],
        )
    )

    story.append(Paragraph("Step 3 — Avatar + Assembly (HeyGen)", s["h3"]))
    story.append(
        Paragraph(
            "HeyGen is where everything comes together. You import your avatar, previous HeyGen videos, "
            "cinematic clips, and ElevenLabs audio.",
            s["body"],
        )
    )
    for f in [
        "Reels (15-30 seconds)",
        "Shorts (30-60 seconds)",
        "TikToks (up to 3 minutes)",
        "YouTube videos up to 3 minutes",
    ]:
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{f}", s["bullet"]))
    story.append(
        Paragraph("HeyGen's multi-scene editor makes this easy.", s["body"])
    )

    story.append(Paragraph("Step 4 — Export & Polish", s["h3"]))
    for f in [
        "9:16 export for Reels and Shorts",
        "16:9 export for YouTube",
        "Optional polish in CapCut or Premiere Pro",
    ]:
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{f}", s["bullet"]))

    story.append(PageBreak())

    # === Section 5: Developer Compatibility ===
    story.append(_section_banner("5. Developer Compatibility", IVAI_GREEN, s))
    story.append(Spacer(1, 0.2 * inch))
    story.append(
        Paragraph(
            "Your entire technical stack is 100% compatible with all platforms.",
            s["body"],
        )
    )
    check_style = ParagraphStyle(
        "check_cell",
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=14,
        textColor=IVAI_GREEN,
        alignment=TA_CENTER,
    )
    chk = Paragraph("&#10003;", check_style)
    compat_table = Table(
        [
            ["Platform", "Node.js", "Python", "PowerShell", "GitHub", "VS Code"],
            ["HeyGen", chk, chk, chk, chk, chk],
            ["Runway Gen-4.5", chk, chk, chk, chk, chk],
            ["ElevenLabs", chk, chk, chk, chk, chk],
            ["Sora 2", chk, chk, chk, chk, chk],
        ],
        colWidths=[1.8 * inch, 1.04 * inch, 1.04 * inch, 1.04 * inch, 1.04 * inch, 1.04 * inch],
        repeatRows=1,
    )
    compat_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), IVAI_GREEN),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 10),
                ("ALIGN", (1, 0), (-1, -1), "CENTER"),
                ("ALIGN", (0, 0), (0, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("FONTNAME", (0, 1), (0, -1), "Helvetica"),
                ("FONTSIZE", (0, 1), (0, -1), 10),
                ("TEXTCOLOR", (0, 1), (0, -1), DARK_TEXT),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT_GRAY]),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#D6DCE2")),
            ]
        )
    )
    story.append(compat_table)
    story.append(Spacer(1, 0.1 * inch))
    story.append(
        Paragraph(
            "No plugins needed. No special setup. Everything works out of the box.",
            s["body"],
        )
    )

    # === Section 6: Cost Summary ===
    story.append(Spacer(1, 0.25 * inch))
    story.append(_section_banner("6. Cost Summary", IVAI_BLUE, s))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("Core Stack", s["h3"]))
    story.append(
        _styled_table(
            [
                ["Platform", "Plan", "Monthly Cost"],
                ["HeyGen", "Business", "~$89"],
                ["Runway Gen-4.5", "Pro", "~$35"],
                ["ElevenLabs", "Creator", "~$22"],
                ["Sora 2 (optional)", "Enterprise", "Varies"],
            ],
            col_widths=[2.4 * inch, 2.3 * inch, 2.3 * inch],
            header_color=IVAI_BLUE,
        )
    )

    story.append(Spacer(1, 0.15 * inch))
    story.append(Paragraph("Extras", s["h3"]))
    story.append(
        _styled_table(
            [
                ["Tool", "Cost"],
                ["CapCut", "Free"],
                ["Premiere Pro", "$20-$35 / mo"],
                ["LUT Packs", "$10-$40"],
                ["Stock Music", "$15-$16 / mo"],
                ["Cloud Storage", "$2-$10 / mo"],
            ],
            col_widths=[3.5 * inch, 3.5 * inch],
            header_color=IVAI_GREEN,
        )
    )

    story.append(Spacer(1, 0.15 * inch))
    story.append(
        Paragraph(
            "<b>Total Monthly (without Sora 2):</b> approximately <b>$146 - $190</b>.",
            s["callout"],
        )
    )

    # === Section 7: Final Recommendation ===
    story.append(Spacer(1, 0.15 * inch))
    story.append(_section_banner("7. Final Recommendation", IVAI_GREEN, s))
    story.append(Spacer(1, 0.2 * inch))
    story.append(
        Paragraph(
            "For Intelligent Voice AI's commercial marketing needs, the best and easiest stack is:",
            s["body"],
        )
    )
    for f in [
        "<b>HeyGen</b> — main editor and avatar platform",
        "<b>Runway Gen-4.5</b> — cinematic motion engine",
        "<b>ElevenLabs</b> — cloned voice and audio layer",
        "<b>Optional: Sora 2</b> — premium realism",
    ]:
        story.append(Paragraph(f'<font color="#0057A0"><b>&#10003;</b></font>&nbsp;&nbsp;{f}', s["check"]))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph("This setup supports:", s["body"]))
    for f in [
        "Reels",
        "Shorts",
        "TikToks",
        "3-minute YouTube videos",
        "Cinematic commercial content",
        "Full automation via Node.js, Python, and GitHub",
    ]:
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{f}", s["bullet"]))

    # === Signature block ===
    story.append(Spacer(1, 0.4 * inch))
    sig = Table(
        [
            [Paragraph("<b>Prepared By</b>", s["h3"])],
            [Paragraph("Adriana Jadlow", s["body"])],
            [Paragraph("Marketing &amp; Social Media Strategist", s["body"])],
            [Paragraph("Intelligent Voice AI", s["body"])],
        ],
        colWidths=[6.8 * inch],
    )
    sig.setStyle(
        TableStyle(
            [
                ("LINEABOVE", (0, 0), (-1, 0), 1.2, IVAI_BLUE),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    story.append(sig)

    doc.build(story)
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    build()
