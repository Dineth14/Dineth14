"use client";

import { motion } from "framer-motion";
import { fadeUp, staggerContainer } from "@/lib/animations";
import { aboutDomains } from "@/lib/data";

export function About() {
  return (
    <section id="about" className="bg-surface py-24 md:py-32">
      <motion.div
        variants={staggerContainer}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, margin: "-100px" }}
        className="mx-auto grid max-w-[1100px] gap-12 px-6 md:grid-cols-[1fr_0.8fr]"
      >
        {/* Text column */}
        <div className="order-2 md:order-1">
          <motion.span
            variants={fadeUp}
            className="font-mono text-small text-text-muted"
          >
            about
          </motion.span>
          <motion.h2
            variants={fadeUp}
            className="mt-2 font-display text-h2 font-semibold text-text-primary"
          >
            Who I am
          </motion.h2>

          <div className="mt-6 max-w-prose space-y-5 text-text-primary leading-[1.75]">
            <motion.p variants={fadeUp}>
              I&apos;m pursuing Electronics &amp; Electrical Engineering at the
              University of Peradeniya — Sri Lanka&apos;s oldest and most
              rigorous engineering faculty. My research sits at the intersection
              of computer vision and remote sensing: I&apos;ve had a paper
              accepted at IEEE IGARSS 2026 on Visual State Space Model backbones
              for aerial image segmentation, benchmarking Mamba-based
              architectures across LoveDA and ISPRS Potsdam. What drives the
              work is a genuine fascination with how machines can be taught to
              perceive spatial structure the way signal processors think about
              frequency — as structured, decomposable information.
            </motion.p>

            <motion.p variants={fadeUp}>
              Alongside the academic path, I run a startup. Building real
              products under university-scale resource constraints has taught me
              more about engineering tradeoffs than any textbook. It means
              writing code that ships, designing systems that survive users, and
              making decisions with incomplete information — the same skill set
              that makes research reproducible also makes products reliable.
            </motion.p>

            <motion.p variants={fadeUp}>
              Motorsport and design live alongside the technical work.
              raceday.lk is a media brand I built for Sri Lanka&apos;s car
              culture — editorial coverage, race photography, and a community
              that cares about how things look as much as how they perform. I
              think about aesthetics the same way I think about loss functions:
              every detail either contributes to the result or it doesn&apos;t.
            </motion.p>
          </div>

          {/* Skills strip */}
          <motion.div
            variants={fadeUp}
            className="mt-8 flex flex-wrap items-center gap-x-3 gap-y-2 font-mono text-small text-text-muted"
          >
            {aboutDomains.map((domain, i) => (
              <span key={domain} className="flex items-center gap-3">
                {domain}
                {i < aboutDomains.length - 1 && (
                  <span className="text-border">|</span>
                )}
              </span>
            ))}
          </motion.div>
        </div>

        {/* Photo column */}
        <motion.div
          variants={fadeUp}
          className="order-1 flex justify-center md:order-2 md:items-start md:justify-end"
        >
          <div className="relative w-full max-w-[380px]">
            <div className="aspect-[4/5] w-full overflow-hidden rounded-2xl border border-border bg-raised">
              {/* Replace src with your actual photo */}
              <img
                src="/photo.jpg"
                alt="Dineth Nethsara — Electronics Engineer and AI Researcher"
                className="h-full w-full object-cover"
              />
            </div>
          </div>
        </motion.div>
      </motion.div>
    </section>
  );
}
