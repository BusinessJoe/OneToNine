"use client"

import { useEffect } from "react";
import { REST_API, WS_API } from "../../settings";
import { useSudokuStore } from "../zustand/sudokuStore";
import { useSocketStore } from "../zustand/socketStore";

const SudokuLoader = () => {
    const setGrid = useSudokuStore((state) => state.setFixedGrid);
    const setWsUrl = useSocketStore((state) => state.setWsUrl);

    const loadSudoku = async () => {
        const response = await fetch(REST_API + "/sudoku");
        const data = await response.json();
        setGrid(data.grid);
        setWsUrl(WS_API + data.ws_path);
    }

    useEffect(() => {
        loadSudoku();
    }, [])

    return null;
};

export default SudokuLoader;