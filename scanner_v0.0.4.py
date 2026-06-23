from reviewers.eye1_structure import review

def main():
    print()
    print("===== FIVE EYES =====")
    print()

    result = review(".")

    print(f"Files Scanned: {result['files_scanned']}")
    print(f"Total Lines: {result['total_lines']}")

if __name__ == "__main__":
    main()

