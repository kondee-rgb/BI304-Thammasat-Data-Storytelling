import os, sys, shutil, zipfile
sys.stdout.reconfigure(encoding='utf-8')

artifact_dir = r"C:\Users\almond\.gemini\antigravity\brain\414cd179-2d86-4496-a901-061ecc18c932"
workspace_dir = r"d:\BI304"

# 1. Copy screenshots
screenshots = [
    'v9_topic01_enriched_eyebrow.png',
    'v9_topic07_dark_narrative_bridge.png',
    'v9_mobile_topic02_bridge.png',
    'v10_topic04_people_transition_settled.png',
    'v10_topic10_step4_sticky_unclipped.png',
    'v10_topic10_laptop720_unclipped.png',
    'v11_topic05_campus_names_legend.png',
    'v11_topic05_full_view.png',
    'v12_doorway_stage_detail.png',
    'v12_hero_doorway_desktop.png',
    'v12_hero_doorway_mobile.png',
    'v12_topic03_tcas_kpi.png',
    'v12_tcas_kpi_row_clean.png',
    'v13_topic07_step2_vertical.png',
    'v13_transition_07_to_08.png',
    'v13_topic08_stage.png',
    'v13_topic09_stage.png',
    'topic-07_step_2_settled.png',
    'topic-08_step_2_settled.png',
    'topic-09_step_2_settled.png'
]

for s in screenshots:
    src = os.path.join(workspace_dir, 'qa', 'screenshots', s)
    dst = os.path.join(artifact_dir, s)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied {s} to artifact dir.")
    else:
        print(f"Warning: {src} not found.")

# 2. Build updated BI304_Latest_Project.zip
zip_path = os.path.join(workspace_dir, "BI304_Latest_Project.zip")
if os.path.exists(zip_path):
    os.remove(zip_path)

include_dirs = ['assets', 'data', 'qa', 'ver1']
include_files = [
    'index.html', 'package.json', 'RUN_WEB.bat', 'SCROLL_STORY_NOTES_TH.md',
    'TRANSITION_PATCH_APPLY_TH.md', 'README.md'
]

def should_include_file(root, filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext in ['.zip', '.tar', '.gz', '.mp4', '.avi', '.mov']:
        return False
    if 'qa' in root.split(os.sep):
        return ext in ['.py', '.js', '.bat', '.sh', '.md', '.txt', '.sql']
    return True

total_files = 0
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for f in include_files:
        fpath = os.path.join(workspace_dir, f)
        if os.path.exists(fpath):
            zipf.write(fpath, f)
            total_files += 1

    for d in include_dirs:
        dpath = os.path.join(workspace_dir, d)
        if not os.path.exists(dpath):
            continue
        for root, dirs, files in os.walk(dpath):
            dirs[:] = [sub for sub in dirs if sub not in ['.git', 'node_modules', 'archive', 'dist', 'build'] and not sub.endswith('_screens') and sub != 'screenshots']
            for file in files:
                if not should_include_file(root, file):
                    continue
                full_p = os.path.join(root, file)
                rel_p = os.path.relpath(full_p, workspace_dir)
                zipf.write(full_p, rel_p)
                total_files += 1

zip_size_mb = os.path.getsize(zip_path) / (1024 * 1024)
print(f"Created {zip_path} with {total_files} files ({zip_size_mb:.2f} MB)")

# 3. Copy zip to artifact dir
dst_zip = os.path.join(artifact_dir, "BI304_Latest_Project.zip")
shutil.copy2(zip_path, dst_zip)
print(f"Copied updated ZIP to {dst_zip}")
