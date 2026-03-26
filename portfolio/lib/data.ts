// ─── Navigation ───────────────────────────────────────────
export const navLinks = [
  { id: "about", label: "about" },
  { id: "research", label: "research" },
  { id: "projects", label: "projects" },
  { id: "contact", label: "contact" },
] as const;

// ─── About ────────────────────────────────────────────────
export const aboutDomains = [
  "Remote Sensing CV",
  "State Space Models",
  "Embedded Systems",
  "DSP",
  "Power Engineering",
] as const;

// ─── Research ─────────────────────────────────────────────
export interface Publication {
  conference: string;
  status: string;
  title: string;
  abstract: string;
  paperUrl: string | null;
  repoUrl: string | null;
}

export const publications: Publication[] = [
  {
    conference: "IEEE IGARSS 2026",
    status: "Accepted",
    title:
      "Visual State Space Model Backbones for Remote Sensing Image Segmentation",
    abstract:
      "Proposes Mamba-based backbone architectures benchmarked on LoveDA and ISPRS Potsdam datasets across multiple model families including VMamba, MambaVision, and Spatial-Mamba, advancing segmentation for aerial imagery.",
    paperUrl: null,
    repoUrl: "https://github.com/Dineth14",
  },
];

export const ongoingResearch =
  "Currently investigating direction-aligned cross-modal state space models and Retinex-based preprocessing for low-light aerial imagery.";

// ─── Projects ─────────────────────────────────────────────
export interface Project {
  domain: string;
  title: string;
  description: string;
  tags: string[];
  githubUrl: string | null;
  demoUrl: string | null;
  featured?: boolean;
}

export const projects: Project[] = [
  {
    domain: "Remote Sensing · Computer Vision",
    title: "Mamba Segmentation Benchmark",
    description:
      "Systematic benchmark of Vision Mamba architectures for remote sensing segmentation on LoveDA and ISPRS Potsdam datasets. Evaluates VMamba, MambaVision, and Spatial-Mamba backbones with UPerNet decoders.",
    tags: ["PyTorch", "VMamba", "Python", "LoveDA", "ISPRS"],
    githubUrl: "https://github.com/Dineth14",
    demoUrl: null,
    featured: true,
  },
  {
    domain: "Embedded Systems · DSP",
    title: "ESP32 Real-Time Noise Logger",
    description:
      "Full-stack embedded audio classification — ESP32 extracts 7D feature vectors via FFT and Hamming window, classifies with offline k-NN from SPIFFS-stored samples. Python GUI for live monitoring.",
    tags: ["C++", "ESP32", "Python", "k-NN", "DSP"],
    githubUrl: "https://github.com/Dineth14/ESP32-Real-Time-Noise-Logger",
    demoUrl: null,
  },
  {
    domain: "Computer Vision · Deep Learning",
    title: "GAR with Physical Constraints",
    description:
      "Deep group activity recognition augmented with physics-aware constraints. Enforces motion consistency and feasibility bounds within spatiotemporal graph networks.",
    tags: ["PyTorch", "GCN", "Transformers"],
    githubUrl: null,
    demoUrl: null,
  },
  {
    domain: "Computer Vision · Change Detection",
    title: "Vision Mamba Change Detection",
    description:
      "Hybrid VMamba + CNN dual-stream architecture for bi-temporal remote sensing change detection with wavelet-domain feature fusion and edge-aware loss functions.",
    tags: ["PyTorch", "VMamba", "SSM", "LEVIR-CD"],
    githubUrl: null,
    demoUrl: null,
  },
];

// ─── Live Deployments ─────────────────────────────────────
export interface Deployment {
  name: string;
  description: string;
  url: string;
}

export const deployments: Deployment[] = [
  {
    name: "raceday.lk",
    description:
      "Motorsport media brand. Editorial platform and race coverage for Sri Lanka's car culture.",
    url: "https://raceday.lk",
  },
];

// ─── Tech Stack ───────────────────────────────────────────
export interface StackColumn {
  title: string;
  items: string[];
}

export const techStack: StackColumn[] = [
  {
    title: "ML & Computer Vision",
    items: [
      "PyTorch",
      "Mamba / SSMs",
      "Transformers",
      "HuggingFace",
      "OpenCV",
      "NumPy",
      "scikit-learn",
    ],
  },
  {
    title: "Embedded & Systems",
    items: [
      "ESP32",
      "FreeRTOS",
      "Arduino",
      "C/C++",
      "MATLAB",
      "Simulink",
      "Simscape",
    ],
  },
  {
    title: "Signal & Tools",
    items: [
      "DSP",
      "Comm Systems",
      "Power Engineering",
      "Python",
      "Git",
      "Linux",
      "LaTeX",
      "VS Code",
    ],
  },
];

// ─── Contact ──────────────────────────────────────────────
export interface ContactLink {
  label: string;
  url: string;
}

export const contactLinks: ContactLink[] = [
  { label: "Email", url: "mailto:dineth@example.com" },
  { label: "LinkedIn", url: "https://linkedin.com/in/dinethnethsara" },
  { label: "GitHub", url: "https://github.com/Dineth14" },
  { label: "Instagram", url: "https://instagram.com/dinethnethsara" },
];
