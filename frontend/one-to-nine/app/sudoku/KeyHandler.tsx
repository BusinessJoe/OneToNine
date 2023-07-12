"use client"

import React from "react";
import { useEffect } from "react";
import { useSudokuStore } from "../zustand/store";

const KeyHandler = ({ children }: { children: React.JSX.Element }) => {
    const setCellValue = useSudokuStore((state) => state.setCellValue);
    const selectedCell = useSudokuStore((state) => state.selectedCell);

    const handleNumDown = (e: KeyboardEvent) => {
        if (selectedCell) {
            const value = Number(e.key);
            setCellValue(selectedCell[0], selectedCell[1], value);
        }
    }

    const handleDelete = (e: KeyboardEvent) => {
        if (selectedCell) {
            setCellValue(selectedCell[0], selectedCell[1], undefined);
        }
    }

    const handleKeyDown = (e: KeyboardEvent) => {
        if ("0" <= e.key && e.key <= "9") {
            handleNumDown(e);
        } else if (e.key === "Backspace") {
            handleDelete(e);
        }
        console.log(e)
    };

    useEffect(() => {
        document.addEventListener("keydown", handleKeyDown);
        return () => {
            document.removeEventListener("keydown", handleKeyDown);
        }
    }, [handleKeyDown])

    return (
        <div onKeyDown={(e) => console.log(e)}>
            {children}
        </div>
    );
};

export default KeyHandler;