"use client"

import { useEffect } from "react";
import { BACKEND_URL } from "../../settings";
import { useSudokuStore } from "../zustand/store";

const SudokuLoader = () => {
    const setGrid = useSudokuStore((state) => state.setFixedGrid);
    const loadSudoku = async () => {
        const response = await fetch(BACKEND_URL + "/sudoku");
        const data = await response.json();
        setGrid(data.grid);
    }

    useEffect(() => {
        loadSudoku();
    }, [])

    return null;
};

export default SudokuLoader;