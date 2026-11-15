#!/usr/bin/env python3
"""
ZDOS Security Agent
Agente autonomo che protegge l'ecosistema ZDOS.

- Intercetta richieste in entrata
- Comunica con K.I.R.A.
- Cattura dati di attacco su file
- Applica decisioni di policy
"""

import json
import time
from pathlib import Path
from datetime import datetime

LOG_DIR = Path("logs")
ATTACK_LOG = LOG_DIR / "attacks.jsonl"

class ZDOSSecurityAgent:
    def __init__(self):
        LOG_DIR.mkdir(exist_ok=True)
        self.version = "0.1.0-lab"

    def capture(self, event: dict):
        """Scrive l'evento di attacco/sospetto su file."""
        event["captured_at"] = datetime.utcnow().isoformat() + "Z"
        event["agent"] = self.version
        with ATTACK_LOG.open("a") as f:
            f.write(json.dumps(event) + "\n")
        print(f"[CAPTURE] {event.get('type', 'unknown')} -> {ATTACK_LOG}")

    def notify_kira(self, payload: dict) -> dict:
        """Stub di comunicazione con K.I.R.A."""
        # In produzione: IPC, socket, o chiamata al processo KIRA
        print(f"[KIRA] invio: {payload.get('type')}")
        # Risposta simulata
        return {
            "action": "log_and_monitor",
            "confidence": 0.8,
            "note": "stub laboratorio"
        }

    def handle_request(self, request: dict) -> dict:
        """Punto di ingresso per ogni richiesta esterna."""
        print(f"[AGENT] richiesta da {request.get('src', 'unknown')}")

        suspicious = request.get("suspicious", False) or request.get("anomaly_score", 0) > 0.7

        if suspicious:
            self.capture({
                "type": "suspicious_request",
                "src": request.get("src"),
                "payload_hash": request.get("payload_hash"),
                "details": request
            })
            decision = self.notify_kira(request)
            return {
                "allowed": decision.get("action") != "block",
                "decision": decision,
                "captured": True
            }

        return {"allowed": True, "captured": False}

def main():
    agent = ZDOSSecurityAgent()
    print(f"ZDOS Security Agent {agent.version} avviato")

    # Demo di laboratorio
    demo = {
        "src": "203.0.113.42",
        "suspicious": True,
        "payload_hash": "abc123",
        "anomaly_score": 0.92
    }
    result = agent.handle_request(demo)
    print(f"Risultato demo: {result}")

if __name__ == "__main__":
    main()
