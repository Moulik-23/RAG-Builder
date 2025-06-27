import os
import shutil
import zipfile
from pathlib import Path

TEMPLATE_DIR = "rag_templates"
DEPLOY_DIR = "deployments"
VSTORE_DIR = "app/vectorstores"  # where embedder stores vector DB

def generate_rag_app(session_id: str, bot_name: str = "my_rag_bot") -> str:
    # Step 1: Define paths
    source_template = Path(TEMPLATE_DIR)
    user_app_path = Path(DEPLOY_DIR) / f"{bot_name}_{session_id}"
    user_vectorstore_path = Path(VSTORE_DIR) / session_id
    target_vectorstore_path = user_app_path / "app" / "sample_data" / "vectorstore"

    # Step 2: Copy rag_templates to user deployment folder
    if user_app_path.exists():
        shutil.rmtree(user_app_path)
    shutil.copytree(source_template, user_app_path)

    # Step 3: Copy vectorstore
    os.makedirs(target_vectorstore_path, exist_ok=True)
    shutil.copytree(user_vectorstore_path, target_vectorstore_path, dirs_exist_ok=True)

    # (Optional) Step 4: Inject bot name into README or config if needed
    readme_path = user_app_path / "README.md"
    if readme_path.exists():
        with open(readme_path, "a") as f:
            f.write(f"\n\n# Bot Name: {bot_name}\nSession ID: {session_id}")

    # Step 5: Zip it
    zip_filename = f"{bot_name}_{session_id}.zip"
    zip_path = Path(DEPLOY_DIR) / zip_filename
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(user_app_path):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(user_app_path)
                zipf.write(file_path, arcname)

    return str(zip_path)
