#!/usr/bin/env python3
"""
ZDOS Security Agent
Agente autonomo che protegge l'ecosistema ZDOS.

- Intercetta richieste
- Cattura su file (audit)
- Comunica con K.I.R.A.
- Prepara record tipizzati per DSN (security-event)
"""

import json
from pathlib import Path
from datetime import datetime

LOG_DIR = Path("logs")
ATTACK_LOG = LOG_DIR / "attacks.jsonl"

class ZDOSSecurityAgent:
    def __init__(self):
        LOG_DIR.mkdir(exist_ok=True)
        self.version = "0.2.0-lab"

    def capture(self, event: dict):
        event["captured_at"] = datetime.utcnow().isoformat() + "Z"
        event["agent"] = self.version
        with ATTACK_LOG.open("a") as f:
            f.write(json.dumps(event) + "\n")
        print(f"[CAPTURE] {event.get('type', 'unknown')} -> {ATTACK_LOG}")

    def to_dsn_record(self, event: dict) -> dict:
        """Converte un evento in record tipizzato DSN."""
        return {
            "type": "security-event",
            "src_ip": event.get("src"),
            "anomaly_score": event.get("anomaly_score", 0),
            "details": event.get("details", {}),
            "action": "log_and_monitor",
            "agent_version": self.version
        }

    def notify_kira(self, payload: dict) -> dict:
        print(f"[KIRA] invio: {payload.get('type')}")
        return {
            "action": "log_and_monitor",
            "confidence": 0.8,
            "note": "stub laboratorio"
        }

    def handle_request(self, request: dict) -> dict:
        print(f"[AGENT] richiesta da {request.get('src', 'unknown')}")

        suspicious = request.get("suspicious", False) or request.get("anomaly_score", 0) > 0.7

        if suspicious:
            captured = {
                "type": "suspicious_request",
                "src": request.get("src"),
                "payload_hash": request.get("payload_hash"),
                "details": request,
                "anomaly_score": request.get("anomaly_score")
            }
            self.capture(captured)
            dsn_record = self.to_dsn_record(captured)
            print(f"[DSN] record pronto: {dsn_record['type']}")
            decision = self.notify_kira(request)
            return {
                "allowed": decision.get("action") != "block",
                "decision": decision,
                "captured": True,
                "dsn_record": dsn_record
            }

        return {"allowed": True, "captured": False}

def main():
    agent = ZDOSSecurityAgent()
    print(f"ZDOS Security Agent {agent.version} avviato")

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
