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
        ink: "#060810",
        surface: "#0d1a2d",
        panel: "#10213a",
        cyan: "#00e7ff",
        ember: "#ff6b35",
        mist: "#f0f4f8",
        muted: "#64748b",
      },
      fontFamily: {
        display: ["var(--font-syne)"],
        mono: ["var(--font-jetbrains-mono)"],
      },
      boxShadow: {
        signal: "0 0 0 1px rgba(0, 231, 255, 0.22), 0 0 24px rgba(0, 231, 255, 0.14)",
        ember: "0 0 0 1px rgba(255, 107, 53, 0.24), 0 0 28px rgba(255, 107, 53, 0.14)",
      },
      animation: {
        "pulse-soft": "pulseSoft 2.6s ease-in-out infinite",
        "float-slow": "floatSlow 8s ease-in-out infinite",
        "scan-line": "scanLine 12s linear infinite",
        radar: "radar 7s linear infinite",
        shimmer: "shimmer 2.2s ease-in-out infinite",
      },
      keyframes: {
        pulseSoft: {
          "0%, 100%": { opacity: "0.45", transform: "scale(1)" },
          "50%": { opacity: "1", transform: "scale(1.04)" },
        },
        floatSlow: {
          "0%, 100%": { transform: "translateY(0px)" },
          "50%": { transform: "translateY(-12px)" },
        },
        scanLine: {
          "0%": { transform: "translateX(-100%)" },
          "100%": { transform: "translateX(150%)" },
        },
        radar: {
          "0%": { transform: "rotate(0deg)" },
          "100%": { transform: "rotate(360deg)" },
        },
        shimmer: {
          "0%, 100%": { opacity: "0.3" },
          "50%": { opacity: "0.95" },
        },
      },
      backgroundImage: {
        grid: "linear-gradient(rgba(0, 231, 255, 0.08) 1px, transparent 1px), linear-gradient(90deg, rgba(0, 231, 255, 0.08) 1px, transparent 1px)",
      },
    },
  },
  plugins: [],
};

export default config;
