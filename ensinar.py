def genMatrix(size: int) -> list:
    matrix: list = []

    for rows in range(size):
        row: list = []

        for items in range(size):
            row.append(items)

        matrix.append(row)

    return matrix


def handleCases(matrix: list, case: str) -> float:
    soma: float = 0
    lPointer: int = 0
    rPointer: int = 11
    divisores: int = 0
    
    for rows in matrix:
        for item in range(5):
            subList: list = rows[lPointer:rPointer]
            soma += sum(subList)
            divisores += len(subList)

        lPointer += 1
        rPointer -= 1


def main(): 
    pass


if __name__ == "__main__":
    main()