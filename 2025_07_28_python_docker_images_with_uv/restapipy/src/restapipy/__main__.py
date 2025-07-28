import uvicorn


def main() -> None:
    uvicorn.run(
        "restapipy.main:app",
        host="0.0.0.0",
        port=9876,
        log_level="info",
        reload=False,
    )


if __name__ == "__main__":
    main()
