"use client"

import { useEffect } from "react";
import { useSudokuStore } from "../zustand/sudokuStore";

const Validator = () => {
    const fixedGrid = useSudokuStore((state) => state.fixedGrid);
    const userGrid = useSudokuStore((state) => state.userGrid);
    const clearErrors = useSudokuStore((state) => state.clearErrors);
    const setError = useSudokuStore((state) => state.setError);

    const mergedGrid: (number | undefined)[][] = Array.from({ length: 11 }, () => Array.from({ length: 11 }, () => undefined));
    for (let row = 1; row <= 9; row++) {
        for (let col = 1; col <= 9; col++) {
            mergedGrid[row][col] = fixedGrid[row][col] ?? userGrid[row][col];
        }
    }

    const validateRow = (row: number) => {
        const counts = Array(10).fill(0);

        for (let col = 1; col <= 9; col++) {
            const value = mergedGrid[row][col];
            if (value !== undefined) {
                counts[value]++
            }
        }

        for (let col = 1; col <= 9; col++) {
            const value = mergedGrid[row][col];
            if (value !== undefined && counts[value] > 1) {
                setError(row, col, true);
            }
        }
    }

    const validateCol = (col: number) => {
        const counts = Array(10).fill(0);

        for (let row = 1; row <= 9; row++) {
            const value = mergedGrid[row][col];
            if (value !== undefined) {
                counts[value]++
            }
        }

        for (let row = 1; row <= 9; row++) {
            const value = mergedGrid[row][col];
            if (value !== undefined && counts[value] > 1) {
                setError(row, col, true);
            }
        }
    }

    const validateBox = (box: number) => {
        const counts = Array(10).fill(0);

        const rowCorner = Math.floor((box - 1) / 3) * 3 + 1;
        const colCorner = ((box - 1) % 3) * 3 + 1;
        for (let row = rowCorner; row < rowCorner + 3; row++) {
            for (let col = colCorner; col < colCorner + 3; col++) {
                const value = mergedGrid[row][col];
                if (value !== undefined) {
                    counts[value]++
                }
            }
        }

        for (let row = rowCorner; row < rowCorner + 3; row++) {
            for (let col = colCorner; col < colCorner + 3; col++) {
                const value = mergedGrid[row][col];
                if (value !== undefined && counts[value] > 1) {
                    setError(row, col, true);
                }
            }
        }
    }

    useEffect(() => {
        clearErrors();
        for (let i = 1; i <= 9; i++) {
            validateRow(i);
            validateCol(i);
            validateBox(i);
        }
    }, [mergedGrid]);

    return null;
};

export default Validator;