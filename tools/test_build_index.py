"""목차 형식과 직접 편집 결과를 검증하는 표준 라이브러리 테스트."""

import unittest

import build_index as index


def entry(date, stage="ML", subject="배운 내용"):
    return {"date": date, "month": date[:7], "stage": stage, "subject": subject}


class IndexTests(unittest.TestCase):
    def test_recent_three_newest_first(self):
        entries = [entry(f"2026-09-{day:02}") for day in range(1, 5)]
        recent = index.render_readme_index(entries).split("## 02 / 월별 아카이브")[0]
        self.assertNotIn("2026-09-01", recent)
        self.assertLess(recent.index("2026-09-04"), recent.index("2026-09-03"))
        self.assertLess(recent.index("2026-09-03"), recent.index("2026-09-02"))

    def test_recent_single_entry(self):
        self.assertEqual(index.render_readme_index([entry("2026-09-01")]).count("**[2026-09-01]"), 1)

    def test_month_neighbors_skip_absent_month(self):
        text = index.render_month_index("2026-09", [entry("2026-09-01")], ["2026-07", "2026-09", "2026-11"])
        self.assertIn("[← 2026-07](../2026-07/README.md)", text)
        self.assertIn("[2026-11 →](../2026-11/README.md)", text)
        self.assertNotIn("2026-08", text)
        self.assertIn("[**01일**](./2026-09-01.md)", text)
        self.assertNotIn("[보기]", text)

    def test_single_month_has_no_neighbor(self):
        text = index.render_month_index("2026-09", [entry("2026-09-01")], ["2026-09"])
        self.assertNotIn("←", text)
        self.assertNotIn("→", text)

    def test_month_tag_tie_preserves_first_occurrence(self):
        text = index.render_readme_index([entry("2026-09-01", "Stats / ML"), entry("2026-09-02", "ML / Stats")])
        self.assertIn("| Stats · ML |", text)

    def test_topic_tie_and_anchor_order(self):
        text = index.render_topics([entry("2026-09-01", "Stats / ML")])
        self.assertIn("[ML (1)](#topic-1) · [Stats (1)](#topic-2)", text)
        self.assertIn('<a id="topic-1"></a>\n\n### ML (1건)', text)

    def test_readme_latest_includes_source_stage(self):
        text = index.render_readme_index([entry("2026-09-01", "Stats / ML", "모델 검증")])
        self.assertIn("**[2026-09-01](./2026-09/2026-09-01.md)** · Stats / ML\n\n모델 검증", text)
        self.assertIn('<a id="latest"></a>', text)
        self.assertIn('<a id="archive"></a>', text)

    def test_month_archive_is_newest_first(self):
        text = index.render_readme_index([entry("2026-08-01"), entry("2026-09-01")])
        archive = text.split("## 02 / 월별 아카이브")[1]
        self.assertLess(archive.index("2026-09"), archive.index("2026-08"))
        self.assertIn("| [**2026-09 →**](./2026-09/README.md) | 1건 | ML |", archive)

    def test_month_rows_are_newest_first_with_stage(self):
        text = index.render_month_index("2026-09", [entry("2026-09-01"), entry("2026-09-02", "Stats / ML", "검증")], ["2026-09"])
        self.assertLess(text.index("[**02일**]"), text.index("[**01일**]"))
        self.assertIn("검증<br>Stats / ML |", text)
        self.assertIn("| 날짜 | 기록 / 단계 |", text)

    def test_topic_entries_include_summaries_and_full_dates(self):
        text = index.render_topics([entry("2026-09-01", "ML", "첫 질문"), entry("2026-09-02", "ML", "다음 질문")])
        self.assertIn("- [2026-09-02](../2026-09/2026-09-02.md) · 다음 질문", text)
        self.assertLess(text.index("- [2026-09-02]"), text.index("- [2026-09-01]"))

    def test_rendering_does_not_change_source_metadata(self):
        entries = [entry("2026-09-01", "Stats / ML", "가" * 120)]
        original = [e.copy() for e in entries]
        index.render_readme_index(entries)
        index.render_month_index("2026-09", entries, ["2026-09"])
        index.render_topics(entries)
        self.assertEqual(entries, original)

    def test_shortening_boundary(self):
        self.assertEqual(index.shorten("가" * 90), "가" * 90)
        self.assertEqual(index.shorten("가" * 91), "가" * 89 + "…")

    def test_replacement_preserves_backslashes_and_surroundings(self):
        text = f"before\n{index.INDEX_BEGIN}\nold\n{index.INDEX_END}\nafter\n"
        block = r"$\alpha$ and C:\notes"
        self.assertEqual(index.replace_index_block(text, block), f"before\n{index.INDEX_BEGIN}\n\n{block}\n\n{index.INDEX_END}\nafter\n")

    def test_missing_marker_fails(self):
        with self.assertRaises(SystemExit):
            index.replace_index_block("no marker", "replacement")


if __name__ == "__main__":
    unittest.main()
