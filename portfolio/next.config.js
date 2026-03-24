/** @type {import('next').NextConfig} */
const isProd = process.env.NODE_ENV === "production";

const nextConfig = {
  output: "export",
  ...(isProd
    ? {
        basePath: "/portfolio",
        assetPrefix: "/portfolio/",
      }
    : {}),
  images: {
    unoptimized: true,
    remotePatterns: [
      {
        protocol: "https",
        hostname: "github-readme-stats.vercel.app",
      },
      {
        protocol: "https",
        hostname: "github-readme-streak-stats.herokuapp.com",
      },
      {
        protocol: "https",
        hostname: "github-readme-activity-graph.vercel.app",
      },
    ],
  },
  reactStrictMode: true,
};

module.exports = nextConfig;
