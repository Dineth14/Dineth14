"use client";

import { motion } from "framer-motion";
import { fadeUp, staggerContainer, cardHover } from "@/lib/animations";
import { projects, deployments } from "@/lib/data";

export function Projects() {
  return (
    <section id="projects" className="bg-surface py-24 md:py-32">
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
          projects
        </motion.span>
        <motion.h2
          variants={fadeUp}
          className="mt-2 font-display text-h2 font-semibold text-accent-light"
        >
          Selected Work
        </motion.h2>

        {/* Project grid */}
        <div className="mt-10 grid gap-6 md:grid-cols-2">
          {projects.map((project) => (
            <motion.article
              key={project.title}
              variants={fadeUp}
              whileHover={cardHover}
              className={`group rounded-xl border border-border bg-deep p-8 transition-colors duration-200 hover:border-accent-subtle hover:bg-raised ${
                project.featured ? "md:col-span-2" : ""
              } ${project.featured ? "border-l-2 border-l-accent-subtle" : ""}`}
            >
              {/* Domain tag */}
              <span className="inline-block rounded-full bg-raised px-2.5 py-0.5 font-mono text-[0.7rem] text-text-muted">
                {project.domain}
              </span>

              {/* Title */}
              <h3
                className={`mt-3 font-display font-semibold text-text-primary ${
                  project.featured ? "text-[1.35rem]" : "text-h3"
                }`}
              >
                {project.title}
              </h3>

              {/* Description */}
              <p className="mt-2 max-w-prose text-small leading-[1.75] text-text-secondary line-clamp-2">
                {project.description}
              </p>

              {/* Tech tags */}
              <div className="mt-4 flex flex-wrap gap-2">
                {project.tags.map((tag) => (
                  <span
                    key={tag}
                    className="rounded bg-raised px-2 py-0.5 font-mono text-[0.75rem] text-text-muted"
                  >
                    {tag}
                  </span>
                ))}
              </div>

              {/* Links */}
              <div className="mt-4 flex items-center gap-4">
                {project.githubUrl && (
                  <a
                    href={project.githubUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-1 text-small text-accent-primary transition-colors hover:text-accent-light"
                  >
                    GitHub <span className="text-xs">↗</span>
                  </a>
                )}
                {project.demoUrl && (
                  <a
                    href={project.demoUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-1 text-small text-accent-primary transition-colors hover:text-accent-light"
                  >
                    Demo <span className="text-xs">↗</span>
                  </a>
                )}
              </div>
            </motion.article>
          ))}
        </div>

        {/* Live Deployments */}
        {deployments.length > 0 && (
          <>
            <motion.div variants={fadeUp} className="mt-12">
              <div className="mb-6 h-px w-full bg-border" />
              <h3 className="font-display text-[1rem] font-medium text-text-secondary">
                Live &amp; Deployed
              </h3>
            </motion.div>

            <div className="mt-4 space-y-3">
              {deployments.map((dep) => (
                <motion.div
                  key={dep.name}
                  variants={fadeUp}
                  className="flex flex-col gap-1 sm:flex-row sm:items-center sm:gap-3"
                >
                  <span className="font-display text-small font-medium text-text-primary">
                    {dep.name}
                  </span>
                  <span className="hidden text-text-muted sm:inline">—</span>
                  <span className="text-small text-text-secondary">
                    {dep.description}
                  </span>
                  <a
                    href={dep.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-1 text-small text-accent-warm transition-colors hover:text-accent-warm/80"
                  >
                    Live <span className="text-xs">↗</span>
                  </a>
                </motion.div>
              ))}
            </div>
          </>
        )}
      </motion.div>
    </section>
  );
}
