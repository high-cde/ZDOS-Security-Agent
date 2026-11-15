# Architettura ZDOS-Security-Agent

## Ruolo

Processo autonomo che si interpone tra il mondo esterno e i componenti interni dell'ecosistema ZDOS (nodi DSN, ZComm, Æsir, zBAG, applicazioni, K.I.R.A.).

## Flusso

```
Richiesta esterna
    → Security Agent (intercettazione + scoring)
        → se sospetta: cattura su file + notifica K.I.R.A.
        ← decisione da K.I.R.A. (allow / monitor / block)
    → risposta al chiamante o blocco
```

## Integrazione

- Può essere invocato via API locale, socket Unix, o come middleware.
- I nodi DSN e ZComm possono inoltrare le richieste in entrata all'agente.
- K.I.R.A. riceve eventi e può restituire policy aggiornate.

## Cattura

File `logs/attacks.jsonl` (JSON Lines) con timestamp, sorgente, hash e dettagli.

## Maturità

M1 (Prototype). Avanzamento solo dopo prove osservabili.
