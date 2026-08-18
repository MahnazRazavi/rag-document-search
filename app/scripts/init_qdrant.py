from app.services.qdrant_service import QdrantService


def main():
    qdrant = QdrantService()

    qdrant.create_collection()

    print("Qdrant collection initialized.")


if __name__ == "__main__":
    main()
