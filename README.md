# ZDOS-Security-Agent

Agente di sicurezza **autonomo** che tutela l'intero ecosistema ZDOS.

Non è legato a hardware specifico (né al Compaq e660). È un servizio/processo che può girare su nodi ZDOS, VPS, o insieme a K.I.R.A.

## Funzioni

- **Protezione multitasking** dell'ecosistema da minacce esterne.
- Intercettazione di tutte le richieste in entrata.
- Comunicazione bidirezionale con **K.I.R.A.** (analisi e policy).
- Cattura su file dei dati di attacco / richieste sospette.
- Gate e logging centralizzato.

## Stato

Prototipo di laboratorio (M1). Segue la policy di verità ZDOS.

## Avvio

```sh
python3 agent/security_agent.py
```

## Componenti

- `agent/security_agent.py` — agente principale
- `docs/ARCHITECTURE.md` — architettura
- `docs/KIRA-BRIDGE.md` — protocollo con K.I.R.A.
- `logs/` — destinazione cattura (esempio)

## Integrazione

Può essere chiamato dai nodi DSN, da ZComm, da Æsir o da qualsiasi componente ZDOS che riceve traffico esterno.
