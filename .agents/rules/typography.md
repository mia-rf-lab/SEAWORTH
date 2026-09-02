---
description: 海沃控股 (SEAWORTH) 全站字體與字級設計系統規範 (Typography Design System)
trigger: always_on
---

# SEAWORTH Typography Design System
這份文件定義了海沃控股 (SEAWORTH) 專案的全站字體與字級規範。當 AI 代理人（Assistant/Agent）在進行任何前端切版、樣式新增或全站調整時，**必須**強制遵守以下變數與規範，禁止使用未經定義的絕對數值（如 `font-size: 20px;` 或 `1.2rem`）。

## 1. 全站字體 (Font Families)
請一律使用宣告在 `:root` 中的變數來設定字體，禁止直接寫死字體名稱。
- `var(--font-display)` (Cormorant Garamond)：用於英文專屬的古典詩意字體（大寫英文標題、裝飾字母）。
- `var(--font-serif)` (Noto Serif TC)：用於中文主標題、副標題與引言（帶有優雅、沉穩氣質）。
- `var(--font-sans)` (Montserrat & Noto Sans TC)：用於大量閱讀的內文、選單、按鈕、小標籤（全站預設字體）。

## 2. 標準字級變數 (Typography Scale)
切版時，文字大小 `font-size` 只能使用以下 12 個定義好的 CSS 變數，禁止使用 `px` 或不規則的 `rem`。

### 巨型裝飾與大標題
- `var(--text-giga)` (14rem / 約 168pt)：極大裝飾字（例如背景浮水印數字）。
- `var(--text-mega)` (10rem / 約 120pt)：背景裝飾字。
- `var(--text-hero)` (6rem / 約 72pt)：網站第一屏 (Hero Section) 超大主標題。

### 區塊標題 (Headings)
- `var(--text-4xl)` (3.8rem / 約 46pt)：各區塊的特大標題。
- `var(--text-3xl)` (3.2rem / 約 38pt)：最常見的區塊 H2 主標題（例如 NEWS & INSIGHTS）。
- `var(--text-2xl)` (2.2rem / 約 26pt)：H3 副標題。
- `var(--text-xl)` (1.8rem / 約 22pt)：H4 小標題。

### 內文與輔助說明 (Body & Utility)
- `var(--text-lg)` (1.35rem / 約 16pt)：偏大的內文、卡片主標題、引言文字。
- `var(--text-base)` (1rem / 約 12pt)：**全站預設標準內文**（適合一般段落閱讀）。
- `var(--text-sm)` (0.9rem / 約 11pt)：稍小的內文（適合按鈕、表單輸入框、選單）。
- `var(--text-xs)` (0.8rem / 約 10pt)：卡片的描述文字、輔助說明。
- `var(--text-tiny)` (0.72rem / 約 9pt)：極小標籤（如日期標籤、裝飾性英文副標題）。

## 3. 實作指示 (AI 執行守則)
1. **禁止硬編碼 (No Hardcoding)**：當要求「字體放大一點」或「字體縮小一點」時，請沿著這份 Scale 往上或往下尋找最適合的變數（例如將 `var(--text-base)` 改為 `var(--text-lg)`），絕對不要自行創造 `1.15rem` 或 `18px` 等數值。
2. **顏色搭配**：文字顏色也必須使用 CSS 變數（如 `var(--c-ink)`、`var(--c-muted)`、`var(--c-charcoal)`、`var(--c-copper)`），禁止使用 `#000000` 或 `#333333`。
3. **維護 `:root`**：如果未來設計變更需要微調大小，請統一至 `:root` 中修改對應的 `--text-*` 變數數值，不要在個別 class 中覆寫 `font-size`。
