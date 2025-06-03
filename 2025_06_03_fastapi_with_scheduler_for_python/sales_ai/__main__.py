import uvicorn


def main() -> None:
    uvicorn.run(
        "sales_ai.main:app",
        host="0.0.0.0",
        port=5002,
        log_level="info",
        reload=True,
    )


if __name__ == "__main__":
    main()
