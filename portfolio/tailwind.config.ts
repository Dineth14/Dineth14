import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./lib/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        deep: "#080C12",
        surface: "#0D1117",
        raised: "#111827",
        border: "#1F2937",
        accent: {
          primary: "#6B8CAE",
          light: "#93B4D0",
          subtle: "#2A3F54",
          warm: "#B8956A",
          "warm-muted": "#7A5F42",
        },
        text: {
          primary: "#E2E8F0",
          secondary: "#94A3B8",
          muted: "#4B5563",
        },
      },
      fontFamily: {
        display: ["var(--font-sora)", "system-ui", "sans-serif"],
        body: ["var(--font-inter)", "system-ui", "sans-serif"],
        mono: ["var(--font-jetbrains-mono)", "monospace"],
      },
      fontSize: {
        hero: ["clamp(2.5rem, 6vw, 4.5rem)", { lineHeight: "1.1", letterSpacing: "-0.02em" }],
        h2: ["clamp(1.5rem, 3vw, 2.25rem)", { lineHeight: "1.2", letterSpacing: "-0.02em" }],
        h3: ["1.25rem", { lineHeight: "1.4", letterSpacing: "-0.02em" }],
        body: ["1rem", { lineHeight: "1.75" }],
        small: ["0.875rem", { lineHeight: "1.6" }],
      },
      maxWidth: {
        prose: "72ch",
      },
    },
  },
  plugins: [],
};

export default config;
