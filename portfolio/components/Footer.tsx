"use client";

import { motion } from "framer-motion";
import { fadeIn } from "@/lib/animations";

export function Footer() {
  return (
    <motion.footer
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true }}
      variants={fadeIn}
      className="border-t border-border bg-deep py-6"
    >
      <div className="mx-auto flex max-w-[1100px] flex-col items-center justify-between gap-2 px-6 sm:flex-row">
        <span className="text-[0.8rem] text-text-muted">
          Dineth Nethsara © {new Date().getFullYear()}
        </span>
        <span className="text-[0.8rem] text-text-muted">
          Built with Next.js · Deployed on Vercel
        </span>
      </div>
    </motion.footer>
  );
}
