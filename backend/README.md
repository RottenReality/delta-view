## Desarrollo

Desde esta carpeta, inicia la API con:

```powershell
uv run python -m uvicorn main:app --reload
```

La invocación como módulo evita el wrapper `uvicorn.exe`, que puede producir
`uv trampoline failed to canonicalize script path` en Windows.