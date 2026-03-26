"use client";

import { motion } from "framer-motion";
import { fadeUp, staggerContainer } from "@/lib/animations";
import { publications, ongoingResearch } from "@/lib/data";

export function Research() {
  return (
    <section id="research" className="bg-deep py-24 md:py-32">
      <motion.div
        variants={staggerContainer}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, margin: "-100px" }}
        className="mx-auto max-w-[1100px] px-6"
      >
        <motion.span
          variants={fadeUp}
          className="font-mono text-small text-text-muted"
        >
          research
        </motion.span>
        <motion.h2
          variants={fadeUp}
          className="mt-2 font-display text-h2 font-semibold text-accent-light"
        >
          Published Work
        </motion.h2>

        {/* Publication cards */}
        <div className="mt-10 space-y-6">
          {publications.map((pub) => (
            <motion.article
              key={pub.title}
              variants={fadeUp}
              className="rounded-xl border-l-2 border-l-accent-warm-muted bg-surface p-8"
            >
              {/* Conference badge */}
              <div className="mb-4 flex items-center gap-3">
                <span className="inline-block rounded-full bg-accent-subtle px-3 py-1 font-mono text-[0.75rem] text-accent-light">
                  {pub.conference}
                </span>
                <span className="font-mono text-[0.75rem] text-text-muted">
                  · {pub.status}
                </span>
              </div>

              {/* Title */}
              <h3 className="font-display text-h3 font-semibold text-accent-light">
                {pub.title}
              </h3>

              {/* Abstract */}
              <p className="mt-3 max-w-prose text-[0.9rem] leading-[1.75] text-text-secondary">
                {pub.abstract}
              </p>

              {/* Links */}
              <div className="mt-4 flex items-center gap-4">
                {pub.paperUrl && (
                  <a
                    href={pub.paperUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="group inline-flex items-center gap-1 text-small text-accent-warm transition-colors hover:text-accent-warm/80"
                  >
                    Paper
                    <span className="text-xs">↗</span>
                    <span className="block h-px w-0 bg-accent-warm transition-all duration-200 group-hover:w-full" />
                  </a>
                )}
                {pub.repoUrl && (
                  <a
                    href={pub.repoUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="group inline-flex items-center gap-1 text-small text-accent-warm transition-colors hover:text-accent-warm/80"
                  >
                    Repository
                    <span className="text-xs">↗</span>
                  </a>
                )}
              </div>
            </motion.article>
          ))}
        </div>

        {/* Ongoing research line */}
        <motion.p
          variants={fadeUp}
          className="mt-8 max-w-prose text-small italic text-text-secondary"
        >
          {ongoingResearch}
        </motion.p>
      </motion.div>
    </section>
  );
}
