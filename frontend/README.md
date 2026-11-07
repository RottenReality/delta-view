# Delta View: Frontend

React + TypeScript + Vite app that renders the chat UI with the Thesys GenUI SDK (`C1Chat`).

See the [root README](../README.md) for the full project overview and setup.

## Development

```bash
npm install
npm run dev
```

The dev server runs on <http://localhost:3000> and proxies `/api` requests to the backend at <http://localhost:8000> (see `vite.config.ts`).

Other scripts:

- `npm run build`: type-check and build for production
- `npm run lint`: run Oxlint
- `npm run preview`: serve the production build
