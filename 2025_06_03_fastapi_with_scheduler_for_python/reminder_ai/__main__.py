import uvicorn


def main() -> None:
    uvicorn.run(
        "reminder_ai.main:app",
        host="127.0.0.1",
        port=8000,
        log_level="info",
        reload=True,
    )


if __name__ == "__main__":
    main()
