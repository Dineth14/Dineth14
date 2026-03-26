"use client";

import { motion } from "framer-motion";
import { fadeUp, staggerContainer } from "@/lib/animations";
import { techStack } from "@/lib/data";

export function TechStack() {
  return (
    <section id="stack" className="bg-deep py-24 md:py-32">
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
          stack
        </motion.span>

        <div className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {techStack.map((column) => (
            <motion.div
              key={column.title}
              variants={fadeUp}
              className="rounded-xl bg-surface p-6"
            >
              <h3 className="font-display text-small font-medium uppercase tracking-[0.1em] text-accent-light">
                {column.title}
              </h3>
              <ul className="mt-4 space-y-2">
                {column.items.map((item) => (
                  <li
                    key={item}
                    className="flex items-center gap-2 text-[0.9rem] text-text-secondary"
                  >
                    <span className="text-text-muted">·</span>
                    {item}
                  </li>
                ))}
              </ul>
            </motion.div>
          ))}
        </div>
      </motion.div>
    </section>
  );
}
