#!/usr/bin/env python3
"""
Générateur du Hub Vibecoding Mastery
Compile automatiquement tous les fichiers Markdown du workspace dans une application Web interactive moderne (index.html).
"""

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CATALOG = [
    {
        "id": "hub-accueil",
        "category": "Vue d'ensemble",
        "title": "Bienvenue sur le Hub",
        "badge": "Accueil",
        "icon": "home",
        "rel_path": "README.md"
    },
    {
        "id": "formation-hub",
        "category": "Formation",
        "title": "Curriculum & Feuille de Route",
        "badge": "Sommaire",
        "icon": "book-open",
        "rel_path": "formation/README.md"
    },
    {
        "id": "lecon-1-vibecode",
        "category": "Formation",
        "title": "1. Le Guide Ultime du Vibecoding",
        "badge": "Module 1",
        "icon": "sparkles",
        "rel_path": "formation/vibecode.md/README.md"
    },
    {
        "id": "lecon-2-prompt",
        "category": "Formation",
        "title": "2. L'Art du Prompting Technique",
        "badge": "Module 2",
        "icon": "terminal",
        "rel_path": "formation/prompt.md/README.md"
    },
    {
        "id": "lecon-2-prompt-library",
        "category": "Formation",
        "title": "2b. Bibliothèque de Prompts",
        "badge": "Ressource",
        "icon": "copy",
        "rel_path": "formation/prompt.md/prompt_library.md"
    },
    {
        "id": "lecon-3-prd",
        "category": "Formation",
        "title": "3. Le PRD (Cahier des Charges)",
        "badge": "Module 3",
        "icon": "file-text",
        "rel_path": "formation/prd.md/README.md"
    },
    {
        "id": "lecon-3-prd-template",
        "category": "Formation",
        "title": "3b. Modèle Officiel de PRD",
        "badge": "Template",
        "icon": "file-check",
        "rel_path": "formation/prd.md/template_prd.md"
    },
    {
        "id": "lecon-4-ai-agent",
        "category": "Formation",
        "title": "4. Agents IA & Workflows Autonomes",
        "badge": "Module 4",
        "icon": "bot",
        "rel_path": "formation/ai_agent.md/README.md"
    },
    {
        "id": "lecon-5-git",
        "category": "Formation",
        "title": "5. Git & GitHub (Filet de Sécurité)",
        "badge": "Module 5",
        "icon": "git-branch",
        "rel_path": "formation/git_workflow.md/README.md"
    },
    {
        "id": "lecon-6-tech-stack",
        "category": "Formation",
        "title": "6. La Stack Technique Idéale",
        "badge": "Module 6",
        "icon": "layers",
        "rel_path": "formation/tech_stack.md/README.md"
    },
    {
        "id": "lecon-7-deployment",
        "category": "Formation",
        "title": "7. Mettre en Ligne & Déployer",
        "badge": "Module 7",
        "icon": "globe",
        "rel_path": "formation/deployment.md/README.md"
    },
    {
        "id": "projets-hub",
        "category": "Projets",
        "title": "Guide de Démarrage des Projets",
        "badge": "Atelier",
        "icon": "folder-git-2",
        "rel_path": "projets/README.md"
    },
    {
        "id": "recap-fluent",
        "category": "Rétrospectives & Projets",
        "title": "🏮 Rétrospective : Projet Fluent Mandarin",
        "badge": "Masterclass",
        "icon": "award",
        "rel_path": "recap/enseignement_projet_fluent.md"
    }
]

def load_documents():
    docs = []
    loaded_paths = set()
    
    # 1. Charger les documents du CATALOG principal
    for item in CATALOG:
        file_path = os.path.join(BASE_DIR, item["rel_path"].replace("/", os.sep))
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            words = len(content.split())
            reading_time = max(1, round(words / 180))
            docs.append({
                "id": item["id"],
                "category": item["category"],
                "title": item["title"],
                "badge": item["badge"],
                "icon": item["icon"],
                "path": item["rel_path"],
                "content": content,
                "wordCount": words,
                "readingTime": f"{reading_time} min"
            })
            loaded_paths.add(os.path.normpath(file_path))
        else:
            print(f"Attention: fichier introuvable {file_path}")

    # 2. Détection automatique dynamique des futurs fichiers dans 'recap/'
    recap_dir = os.path.join(BASE_DIR, "recap")
    if os.path.exists(recap_dir):
        for root, _, files in os.walk(recap_dir):
            for file in files:
                if file.endswith(".md"):
                    full_p = os.path.normpath(os.path.join(root, file))
                    if full_p not in loaded_paths:
                        with open(full_p, "r", encoding="utf-8") as f:
                            content = f.read()
                        
                        # Extraire le premier titre H1
                        title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                        title = title_match.group(1).strip() if title_match else file.replace(".md", "").replace("_", " ").title()
                        rel_p = os.path.relpath(full_p, BASE_DIR).replace("\\", "/")
                        doc_id = "recap-" + re.sub(r"[^a-zA-Z0-9_-]", "-", file.replace(".md", "")).lower()

                        words = len(content.split())
                        reading_time = max(1, round(words / 180))
                        docs.append({
                            "id": doc_id,
                            "category": "Rétrospectives & Projets",
                            "title": title,
                            "badge": "Enseignement",
                            "icon": "book-marked",
                            "path": rel_p,
                            "content": content,
                            "wordCount": words,
                            "readingTime": f"{reading_time} min"
                        })
                        loaded_paths.add(full_p)
                        print(f"-> Découverte automatique : {rel_p}")

    return docs

def generate_html(docs):
    docs_json = json.dumps(docs, ensure_ascii=False)
    
    html = f"""<!DOCTYPE html>
<html lang="fr" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vibecoding Mastery – Hub de Formation & Projets</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          }},
          colors: {{
            brand: {{
              50: '#eef2ff',
              100: '#e0e7ff',
              400: '#818cf8',
              500: '#6366f1',
              600: '#4f46e5',
              700: '#4338ca',
            }},
            darkbg: {{
              900: '#090d16',
              850: '#0e1424',
              800: '#141d33',
              750: '#19233d',
              700: '#1e2942',
            }}
          }}
        }}
      }}
    }}
  </script>

  <!-- Marked.js (Markdown parser) -->
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  
  <!-- Highlight.js for Code Highlighting -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark-dimmed.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <style>
    /* Custom Scrollbar */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: transparent;
    }}
    ::-webkit-scrollbar-thumb {{
      background: rgba(148, 163, 184, 0.2);
      border-radius: 9999px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: rgba(148, 163, 184, 0.4);
    }}

    /* Markdown Styling */
    .prose-custom {{
      font-size: 1rem;
      line-height: 1.8;
    }}
    .prose-custom h1 {{
      font-size: 2rem;
      font-weight: 800;
      letter-spacing: -0.025em;
      margin-top: 1rem;
      margin-bottom: 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 1px solid rgba(148, 163, 184, 0.15);
      color: inherit;
    }}
    .prose-custom h2 {{
      font-size: 1.45rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      margin-top: 2.25rem;
      margin-bottom: 1rem;
      color: inherit;
      border-bottom: 1px solid rgba(148, 163, 184, 0.08);
      padding-bottom: 0.4rem;
    }}
    .prose-custom h3 {{
      font-size: 1.2rem;
      font-weight: 600;
      margin-top: 1.75rem;
      margin-bottom: 0.75rem;
      color: #818cf8;
    }}
    .prose-custom p {{
      margin-bottom: 1.15rem;
      line-height: 1.75;
      color: #94a3b8;
    }}
    .dark .prose-custom p {{
      color: #cbd5e1;
    }}
    .prose-custom ul, .prose-custom ol {{
      margin-bottom: 1.25rem;
      padding-left: 1.5rem;
      color: #cbd5e1;
    }}
    .prose-custom ul {{ list-style-type: disc; }}
    .prose-custom ol {{ list-style-type: decimal; }}
    .prose-custom li {{ margin-bottom: 0.4rem; line-height: 1.6; }}
    
    .prose-custom blockquote {{
      border-left: 4px solid #6366f1;
      background: rgba(99, 102, 241, 0.08);
      padding: 0.85rem 1.25rem;
      border-radius: 0 0.75rem 0.75rem 0;
      margin: 1.5rem 0;
      color: #e2e8f0;
      font-style: italic;
    }}
    
    .prose-custom table {{
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      margin: 1.5rem 0;
      border-radius: 0.75rem;
      overflow: hidden;
      border: 1px solid rgba(148, 163, 184, 0.15);
    }}
    .prose-custom th {{
      background: rgba(99, 102, 241, 0.12);
      padding: 0.75rem 1rem;
      text-align: left;
      font-weight: 600;
      font-size: 0.875rem;
      border-bottom: 1px solid rgba(148, 163, 184, 0.15);
    }}
    .prose-custom td {{
      padding: 0.75rem 1rem;
      border-bottom: 1px solid rgba(148, 163, 184, 0.1);
      font-size: 0.875rem;
    }}
    .prose-custom tr:last-child td {{
      border-bottom: none;
    }}
    
    .prose-custom a {{
      color: #818cf8;
      text-decoration: underline;
      text-underline-offset: 3px;
      font-weight: 500;
      transition: color 0.15s;
    }}
    .prose-custom a:hover {{
      color: #a5b4fc;
    }}
    
    .prose-custom code:not(pre code) {{
      background: rgba(99, 102, 241, 0.15);
      color: #a5b4fc;
      padding: 0.15rem 0.4rem;
      border-radius: 0.375rem;
      font-size: 0.875em;
      font-family: 'JetBrains Mono', monospace;
    }}

    .reading-bar {{
      position: fixed;
      top: 0;
      left: 0;
      height: 3px;
      background: linear-gradient(90deg, #6366f1, #a855f7);
      width: 0%;
      z-index: 100;
      transition: width 0.1s;
    }}
  </style>
</head>
<body class="bg-slate-50 dark:bg-darkbg-900 text-slate-800 dark:text-slate-100 min-h-screen flex flex-col antialiased selection:bg-brand-500 selection:text-white">
  
  <div id="readingProgress" class="reading-bar"></div>

  <!-- Top Navbar -->
  <header class="sticky top-0 z-40 w-full border-b border-slate-200 dark:border-slate-800/80 bg-white/90 dark:bg-darkbg-900/90 backdrop-blur-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
      
      <!-- Brand & Mobile Toggle -->
      <div class="flex items-center gap-3">
        <button id="mobileMenuBtn" aria-label="Ouvrir le menu" class="md:hidden p-2 rounded-xl bg-slate-100 dark:bg-darkbg-800 text-slate-700 dark:text-slate-300 hover:text-white hover:bg-brand-600 transition flex items-center gap-1.5">
          <i data-lucide="menu" class="w-5 h-5"></i>
          <span class="text-xs font-semibold">Menu</span>
        </button>
        <div class="flex items-center gap-2.5 cursor-pointer" onclick="selectDoc('hub-accueil')">
          <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-brand-600 to-indigo-400 flex items-center justify-center text-white shadow-lg shadow-brand-500/25">
            <i data-lucide="sparkles" class="w-5 h-5"></i>
          </div>
          <div>
            <span class="font-bold text-base tracking-tight text-slate-900 dark:text-white">Vibecoding <span class="text-brand-500">Mastery</span></span>
            <span class="hidden sm:inline-block ml-2 px-2 py-0.5 text-[10px] font-semibold uppercase tracking-wider rounded-full bg-brand-500/10 text-brand-500 border border-brand-500/20">Guide & Lab</span>
          </div>
        </div>
      </div>

      <!-- Center Search Bar -->
      <div class="flex-1 max-w-md hidden sm:block">
        <div class="relative">
          <i data-lucide="search" class="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400"></i>
          <input 
            type="text" 
            id="searchInput" 
            placeholder="Rechercher une leçon, prompt, git, vercel... (Ctrl+K)" 
            class="w-full pl-10 pr-12 py-2 text-sm rounded-xl border border-slate-200 dark:border-slate-700/80 bg-slate-100/70 dark:bg-darkbg-800/80 text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-brand-500/50 transition-all"
          >
          <kbd class="absolute right-3 top-1/2 -translate-y-1/2 px-1.5 py-0.5 text-[10px] font-mono text-slate-400 bg-slate-200 dark:bg-slate-700/60 rounded border border-slate-300 dark:border-slate-600">Ctrl+K</kbd>
        </div>
      </div>

      <!-- Right Controls -->
      <div class="flex items-center gap-2">
        <button id="themeToggleBtn" title="Basculer le thème clair / sombre" class="p-2 rounded-xl text-slate-500 hover:text-slate-800 dark:text-slate-400 dark:hover:text-slate-100 hover:bg-slate-100 dark:hover:bg-darkbg-800 transition-colors">
          <i data-lucide="moon" class="w-5 h-5 hidden dark:block"></i>
          <i data-lucide="sun" class="w-5 h-5 block dark:hidden"></i>
        </button>
        <span class="px-3 py-1 text-xs font-semibold rounded-xl bg-brand-500/10 text-brand-400 border border-brand-500/20 hidden lg:inline-flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          Mode Local Actif
        </span>
      </div>

    </div>
  </header>

  <!-- Main Container -->
  <div class="max-w-7xl mx-auto w-full flex-1 flex px-4 sm:px-6 lg:px-8 relative">
    
    <!-- Sidebar Navigation (Always visible on desktop >= 768px, slide-over on mobile) -->
    <aside id="sidebar" class="fixed md:static inset-y-0 left-0 z-30 w-72 md:w-64 flex-shrink-0 pt-20 md:pt-6 pb-6 px-4 md:px-0 bg-white dark:bg-darkbg-900 md:bg-transparent border-r md:border-r-0 border-slate-200 dark:border-slate-800 overflow-y-auto transform -translate-x-full md:translate-x-0 transition-transform duration-200 ease-in-out shadow-2xl md:shadow-none">
      
      <!-- Mobile Search inside Drawer -->
      <div class="mb-4 sm:hidden">
        <input 
          type="text" 
          id="mobileSearchInput" 
          placeholder="Rechercher..." 
          class="w-full px-3.5 py-2 text-sm rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-100 dark:bg-darkbg-800 text-slate-900 dark:text-slate-100"
        >
      </div>

      <nav id="navContainer" class="space-y-6 pr-2">
        <!-- Rendered via JS -->
      </nav>
    </aside>

    <!-- Overlay for mobile drawer -->
    <div id="drawerOverlay" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-20 hidden md:hidden"></div>

    <!-- Main Content Area -->
    <main class="flex-1 min-w-0 py-6 md:py-8 md:pl-8">
      
      <!-- Article Header -->
      <div class="mb-6 pb-6 border-b border-slate-200 dark:border-slate-800/80">
        <div class="flex flex-wrap items-center gap-2 mb-3">
          <span id="docCategory" class="text-xs font-bold uppercase tracking-wider text-brand-400"></span>
          <span class="text-slate-400 dark:text-slate-600">•</span>
          <span id="docBadge" class="px-2.5 py-0.5 text-xs font-semibold rounded-full bg-slate-100 dark:bg-darkbg-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700"></span>
          <span class="text-slate-400 dark:text-slate-600">•</span>
          <span id="docReadingTime" class="text-xs text-slate-500 dark:text-slate-400 flex items-center gap-1 font-medium">
            <i data-lucide="clock" class="w-3.5 h-3.5"></i>
            <span></span>
          </span>
          <span class="text-slate-400 dark:text-slate-600 hidden sm:inline">•</span>
          <span id="docFilePath" class="text-xs font-mono text-slate-400 truncate hidden sm:inline"></span>
        </div>
        <h1 id="docTitle" class="text-2xl sm:text-3xl md:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight"></h1>
      </div>

      <!-- Rendered Article Body -->
      <article id="docBody" class="prose-custom max-w-none">
        <!-- Content will be inserted here -->
      </article>

      <!-- Next / Previous Navigation -->
      <div class="mt-12 pt-6 border-t border-slate-200 dark:border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4">
        <button id="prevDocBtn" class="w-full sm:w-auto px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700/80 hover:bg-slate-100 dark:hover:bg-darkbg-800 flex items-center gap-2 text-sm font-semibold transition cursor-pointer">
          <i data-lucide="arrow-left" class="w-4 h-4"></i>
          <span id="prevDocLabel">Précédent</span>
        </button>
        <button id="nextDocBtn" class="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-brand-600 hover:bg-brand-500 text-white flex items-center justify-center gap-2 text-sm font-semibold shadow-lg shadow-brand-500/20 transition cursor-pointer">
          <span id="nextDocLabel">Suivant</span>
          <i data-lucide="arrow-right" class="w-4 h-4"></i>
        </button>
      </div>

    </main>

  </div>

  <!-- Toast Notification for Copy -->
  <div id="toast" class="fixed bottom-6 right-6 z-50 transform translate-y-12 opacity-0 pointer-events-none transition-all duration-300 flex items-center gap-2 px-4 py-2.5 rounded-xl bg-slate-900 text-white dark:bg-white dark:text-slate-900 shadow-2xl text-xs font-semibold">
    <i data-lucide="check" class="w-4 h-4 text-emerald-500"></i>
    <span id="toastMsg">Copié dans le presse-papier !</span>
  </div>

  <!-- Embedded Data & Client Scripts -->
  <script>
    const DOCUMENTS = {docs_json};
    let currentDocId = null;

    // Custom marked renderer that supports Marked v12, v13, v14, v15+ safely
    const renderer = new marked.Renderer();
    
    // Robust Code Block Renderer
    renderer.code = function(arg1, arg2) {{
      let text = '';
      let lang = 'plaintext';
      
      // Handle both Marked v12+ token object and older (code, lang) arguments
      if (arg1 && typeof arg1 === 'object') {{
        text = arg1.text || '';
        lang = arg1.lang || 'plaintext';
      }} else {{
        text = String(arg1 || '');
        lang = arg2 || 'plaintext';
      }}

      lang = (lang.trim().split(/\\s+/)[0] || 'plaintext').toLowerCase();
      
      let highlighted = '';
      try {{
        if (typeof hljs !== 'undefined' && hljs.getLanguage(lang)) {{
          highlighted = hljs.highlight(text, {{ language: lang }}).value;
        }} else if (typeof hljs !== 'undefined') {{
          highlighted = hljs.highlightAuto(text).value;
        }} else {{
          highlighted = text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        }}
      }} catch (e) {{
        highlighted = text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      }}

      const escapedCode = encodeURIComponent(text);

      return `
        <div class="code-block-wrapper my-5 rounded-xl overflow-hidden border border-slate-700/60 bg-[#0d1117] shadow-xl">
          <div class="code-header flex items-center justify-between px-4 py-2 bg-slate-800/80 border-b border-slate-700/50 text-xs font-mono text-slate-300">
            <span class="font-bold text-indigo-400 tracking-wider uppercase">${{lang}}</span>
            <button onclick="copyCode(this, '${{escapedCode}}')" class="flex items-center gap-1.5 px-2.5 py-1 rounded bg-slate-700/70 hover:bg-brand-600 text-slate-200 hover:text-white transition cursor-pointer text-xs">
              <i data-lucide="copy" class="w-3.5 h-3.5"></i>
              <span>Copier</span>
            </button>
          </div>
          <pre class="p-4 overflow-x-auto text-sm leading-relaxed"><code class="hljs language-${{lang}}">${{highlighted}}</code></pre>
        </div>
      `;
    }};

    marked.use({{ renderer, gfm: true, breaks: false }});

    // Render Navigation Sidebar
    function renderNavigation(searchFilter = '') {{
      const nav = document.getElementById('navContainer');
      if (!nav) return;
      nav.innerHTML = '';

      const categories = [...new Set(DOCUMENTS.map(d => d.category))];

      categories.forEach(cat => {{
        const filteredDocs = DOCUMENTS.filter(d => 
          d.category === cat && 
          (d.title.toLowerCase().includes(searchFilter.toLowerCase()) || 
           d.content.toLowerCase().includes(searchFilter.toLowerCase()))
        );

        if (filteredDocs.length === 0) return;

        const section = document.createElement('div');
        section.className = 'space-y-1';

        const catTitle = document.createElement('h3');
        catTitle.className = 'px-3 text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-2';
        catTitle.textContent = cat;
        section.appendChild(catTitle);

        filteredDocs.forEach(doc => {{
          const btn = document.createElement('button');
          const isActive = doc.id === currentDocId;
          btn.className = `w-full text-left flex items-center justify-between px-3 py-2.5 rounded-xl text-xs sm:text-sm font-medium transition cursor-pointer ${{
            isActive 
              ? 'bg-brand-600/15 text-brand-400 font-semibold border border-brand-500/30' 
              : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-darkbg-800 hover:text-slate-900 dark:hover:text-slate-100'
          }}`;
          
          btn.innerHTML = `
            <div class="flex items-center gap-2.5 truncate">
              <i data-lucide="${{doc.icon || 'file-text'}}" class="w-4 h-4 flex-shrink-0 text-slate-400"></i>
              <span class="truncate">${{doc.title}}</span>
            </div>
            <span class="text-[10px] px-1.5 py-0.5 rounded bg-slate-200/50 dark:bg-slate-800 text-slate-500 dark:text-slate-400">${{doc.badge}}</span>
          `;

          btn.onclick = () => {{
            selectDoc(doc.id);
            closeMobileDrawer();
          }};

          section.appendChild(btn);
        }});

        nav.appendChild(section);
      }});

      if (window.lucide) lucide.createIcons();
    }}

    // Select and display a document
    function selectDoc(docId) {{
      const doc = DOCUMENTS.find(d => d.id === docId) || DOCUMENTS[0];
      if (!doc) return;

      currentDocId = doc.id;
      window.location.hash = doc.id;

      document.getElementById('docCategory').textContent = doc.category;
      document.getElementById('docBadge').textContent = doc.badge;
      document.getElementById('docReadingTime').querySelector('span').textContent = doc.readingTime;
      document.getElementById('docFilePath').textContent = doc.path;
      document.getElementById('docTitle').textContent = doc.title;

      // Render markdown with try-catch fallback
      try {{
        const htmlContent = marked.parse(doc.content);
        document.getElementById('docBody').innerHTML = htmlContent;
      }} catch (err) {{
        console.error('Erreur parsing Markdown:', err);
        document.getElementById('docBody').innerHTML = `<div class="p-4 bg-red-500/10 border border-red-500/30 rounded-xl text-red-300">Erreur d'affichage du contenu.</div>`;
      }}

      // Handle in-content markdown links to navigate internally
      attachInternalLinkInterceptors();

      // Update Prev / Next buttons
      const currentIndex = DOCUMENTS.findIndex(d => d.id === doc.id);
      const prevDoc = DOCUMENTS[currentIndex - 1];
      const nextDoc = DOCUMENTS[currentIndex + 1];

      const prevBtn = document.getElementById('prevDocBtn');
      const nextBtn = document.getElementById('nextDocBtn');

      if (prevDoc) {{
        prevBtn.style.visibility = 'visible';
        document.getElementById('prevDocLabel').textContent = prevDoc.title;
        prevBtn.onclick = () => selectDoc(prevDoc.id);
      }} else {{
        prevBtn.style.visibility = 'hidden';
      }}

      if (nextDoc) {{
        nextBtn.style.visibility = 'visible';
        document.getElementById('nextDocLabel').textContent = nextDoc.title;
        nextBtn.onclick = () => selectDoc(nextDoc.id);
      }} else {{
        nextBtn.style.visibility = 'hidden';
      }}

      const searchVal = document.getElementById('searchInput') ? document.getElementById('searchInput').value : '';
      renderNavigation(searchVal);
      if (window.lucide) lucide.createIcons();
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    // Intercept clicks on links that reference other files in the project
    function attachInternalLinkInterceptors() {{
      const container = document.getElementById('docBody');
      const links = container.querySelectorAll('a');
      links.forEach(link => {{
        const rawHref = link.getAttribute('href') || '';
        let decodedHref = '';
        try {{
          decodedHref = decodeURIComponent(rawHref).replace(/\\\\/g, '/');
        }} catch(e) {{
          decodedHref = rawHref.replace(/\\\\/g, '/');
        }}

        // Check if link matches any document path or id
        const targetDoc = DOCUMENTS.find(d => 
          decodedHref.endsWith(d.path) || 
          decodedHref.includes(d.path) || 
          (d.id && rawHref === '#' + d.id)
        );

        if (targetDoc) {{
          link.style.cursor = 'pointer';
          link.addEventListener('click', (e) => {{
            e.preventDefault();
            selectDoc(targetDoc.id);
          }});
        }}
      }});
    }}

    // Copy helper
    function copyCode(btn, encodedCode) {{
      const code = decodeURIComponent(encodedCode);
      navigator.clipboard.writeText(code).then(() => {{
        showToast("Code copié dans le presse-papier !");
      }}).catch(() => {{
        // Fallback
        const ta = document.createElement('textarea');
        ta.value = code;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        showToast("Code copié dans le presse-papier !");
      }});
    }}

    function showToast(msg) {{
      const toast = document.getElementById('toast');
      document.getElementById('toastMsg').textContent = msg;
      toast.classList.remove('translate-y-12', 'opacity-0', 'pointer-events-none');
      setTimeout(() => {{
        toast.classList.add('translate-y-12', 'opacity-0', 'pointer-events-none');
      }}, 2500);
    }}

    // Theme toggle
    const themeBtn = document.getElementById('themeToggleBtn');
    themeBtn.addEventListener('click', () => {{
      const isDark = document.documentElement.classList.toggle('dark');
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
      if (window.lucide) lucide.createIcons();
    }});

    // Reading progress bar
    window.addEventListener('scroll', () => {{
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
      document.getElementById('readingProgress').style.width = scrolled + '%';
    }});

    // Search events
    const searchInput = document.getElementById('searchInput');
    const mobileSearchInput = document.getElementById('mobileSearchInput');

    function handleSearch(e) {{
      renderNavigation(e.target.value);
    }}
    if (searchInput) searchInput.addEventListener('input', handleSearch);
    if (mobileSearchInput) mobileSearchInput.addEventListener('input', handleSearch);

    // Keyboard shortcut (Ctrl+K)
    window.addEventListener('keydown', (e) => {{
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {{
        e.preventDefault();
        if (searchInput) searchInput.focus();
      }}
    }});

    // Mobile Drawer Controls
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('drawerOverlay');

    function openMobileDrawer() {{
      sidebar.classList.remove('-translate-x-full');
      overlay.classList.remove('hidden');
    }}
    function closeMobileDrawer() {{
      sidebar.classList.add('-translate-x-full');
      overlay.classList.add('hidden');
    }}
    if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', openMobileDrawer);
    if (overlay) overlay.addEventListener('click', closeMobileDrawer);

    // Initial load
    window.addEventListener('DOMContentLoaded', () => {{
      const initialId = window.location.hash.replace('#', '') || 'hub-accueil';
      selectDoc(initialId);
      if (window.lucide) lucide.createIcons();
    }});
  </script>
</body>
</html>
"""
    return html

def main():
    print("Compilation du Hub Vibecoding Mastery...")
    docs = load_documents()
    print(f"-> {len(docs)} documents chargés avec succès.")
    
    html = generate_html(docs)
    output_file = os.path.join(BASE_DIR, "index.html")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"-> Hub généré avec succès dans : {output_file}")

if __name__ == "__main__":
    main()
