"use client";

import { motion } from "framer-motion";
import { fadeUp, staggerContainer } from "@/lib/animations";
import { contactLinks } from "@/lib/data";

export function Contact() {
  return (
    <section id="contact" className="bg-surface py-24 md:py-32">
      <motion.div
        variants={staggerContainer}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, margin: "-100px" }}
        className="mx-auto max-w-[600px] px-6 text-center"
      >
        <motion.h2
          variants={fadeUp}
          className="font-display text-h2 font-semibold text-text-primary"
        >
          Let&apos;s talk
        </motion.h2>

        <motion.p
          variants={fadeUp}
          className="mt-4 text-text-secondary leading-[1.75]"
        >
          Whether it&apos;s research, a build, or just something
          interesting you&apos;re working on — reach out.
        </motion.p>

        {/* Contact links */}
        <motion.div
          variants={fadeUp}
          className="mt-8 flex flex-wrap items-center justify-center gap-6"
        >
          {contactLinks.map((link) => (
            <a
              key={link.label}
              href={link.url}
              target="_blank"
              rel="noopener noreferrer"
              className="group relative text-accent-light transition-colors duration-200 hover:text-accent-warm"
            >
              {link.label}
              <span className="absolute -bottom-0.5 left-0 h-px w-0 bg-accent-warm transition-all duration-200 group-hover:w-full" />
            </a>
          ))}
        </motion.div>

        {/* Colophon */}
        <motion.p
          variants={fadeUp}
          className="mt-10 font-mono text-[0.8rem] italic text-text-muted"
        >
          Currently in Peradeniya, Sri Lanka — open to research
          collaborations and internship opportunities.
        </motion.p>
      </motion.div>
    </section>
  );
}
