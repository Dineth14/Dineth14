"use client";

import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { fadeUp, staggerContainer } from "@/lib/animations";

export function Hero() {
  const [showChevron, setShowChevron] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => setShowChevron(false), 3000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <section className="relative flex min-h-screen items-center bg-deep">
      {/* Subtle grid pattern */}
      <div
        className="pointer-events-none absolute inset-0"
        style={{
          backgroundImage:
            "linear-gradient(rgba(107,140,174,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(107,140,174,0.03) 1px, transparent 1px)",
          backgroundSize: "80px 80px",
        }}
      />

      {/* Faint radial gradient top-left */}
      <div
        className="pointer-events-none absolute left-0 top-0 h-[600px] w-[600px]"
        style={{
          background:
            "radial-gradient(circle at top left, rgba(42,63,84,0.4), transparent 70%)",
        }}
      />

      <motion.div
        variants={staggerContainer}
        initial="hidden"
        animate="visible"
        className="relative mx-auto w-full max-w-[1100px] px-6"
      >
        {/* Small label */}
        <motion.p
          variants={fadeUp}
          className="mb-4 font-mono text-[0.8rem] text-text-muted"
        >
          Electronics &amp; Electrical Engineer
          <br />
          University of Peradeniya, Sri Lanka
        </motion.p>

        {/* Name */}
        <motion.h1
          variants={fadeUp}
          className="font-display text-hero font-semibold text-text-primary"
        >
          Dineth Nethsara
        </motion.h1>

        {/* Tagline */}
        <motion.p
          variants={fadeUp}
          className="mt-4 max-w-prose text-[1.125rem] leading-relaxed text-text-secondary"
        >
          I build systems that learn to see.
          <br />
          Researcher. Engineer. Founder.
        </motion.p>

        {/* CTAs */}
        <motion.div variants={fadeUp} className="mt-8 flex items-center gap-6">
          <a
            href="#research"
            className="inline-flex items-center gap-2 rounded-lg border border-accent-primary px-5 py-2.5 text-small font-medium text-accent-light transition-colors duration-200 hover:bg-accent-subtle"
          >
            View Research
            <span className="text-xs">↗</span>
          </a>
          <a
            href="#projects"
            className="group inline-flex items-center gap-1.5 text-small text-text-secondary transition-colors duration-200 hover:text-accent-light"
          >
            See Projects
            <span className="inline-block transition-transform duration-200 group-hover:translate-x-0.5">
              →
            </span>
          </a>
        </motion.div>
      </motion.div>

      {/* Scroll anchor chevron */}
      <motion.div
        initial={{ opacity: 1 }}
        animate={{ opacity: showChevron ? 1 : 0 }}
        transition={{ duration: 0.6 }}
        className="absolute bottom-8 left-1/2 -translate-x-1/2"
      >
        <motion.div
          animate={{ y: [0, 4, 0] }}
          transition={{ repeat: Infinity, duration: 1.5, ease: "easeInOut" }}
          className="flex flex-col items-center gap-2"
        >
          <span className="text-[0.75rem] text-text-muted">
            scroll to explore
          </span>
          <svg
            width="16"
            height="16"
            viewBox="0 0 16 16"
            fill="none"
            className="text-text-muted"
          >
            <path
              d="M4 6L8 10L12 6"
              stroke="currentColor"
              strokeWidth="1.5"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        </motion.div>
      </motion.div>
    </section>
  );
}
