# Bridge con K.I.R.A.

Comunicazione bidirezionale di laboratorio tra ZDOS-Security-Agent e K.I.R.A.

## Messaggi verso KIRA

- `SUSPICIOUS_REQUEST` — richiesta intercettata con score elevato
- `ATTACK_CAPTURE` — dati già scritti su file
- `HEARTBEAT` — stato dell'agente

## Messaggi da KIRA

- `POLICY_UPDATE` — nuova regola (block/allow/monitor)
- `ANALYSIS_RESULT` — esito analisi del payload

## Implementazione attuale

Stub in `agent/security_agent.py` (`notify_kira`).  
In produzione: IPC, gRPC, o socket verso il processo K.I.R.A.
