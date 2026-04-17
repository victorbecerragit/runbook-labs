# Contribution Guide

To add a new lab domain to this monorepo:

1. **Create the Folder**: `mkdir -p labs/my-new-lab/{notebooks,data,configs,outputs}`
2. **Add a README**: Create `labs/my-new-lab/README.md` defining the objective.
3. **Add Requirements**: Create `labs/my-new-lab/requirements.txt` with specific library versions.
4. **Notebooks**: Add clean, sequential `.ipynb` files to `labs/my-new-lab/notebooks/`. Start with `00-intro.ipynb`.
5. **Update Catalog**: Add your lab to `docs/catalog.md` and the root `README.md`.
6. **Reusable Code**: If your lab introduces logic useful to others, place it in `shared/python/`.

Always test your lab in the appropriate Codespace devcontainer before proposing changes.
