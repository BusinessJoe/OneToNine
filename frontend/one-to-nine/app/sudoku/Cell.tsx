"use client"

import React from "react";
import { selectCellValue, useSudokuStore } from "../zustand/store";

interface CellProps {
    width: number,
    row: number,
    col: number,
}

const Cell = ({ width, row, col }: CellProps) => {
    const selectedCell = useSudokuStore((state) => state.selectedCell)
    const cellValue = useSudokuStore(selectCellValue(row, col))

    const selectCell = useSudokuStore((state) => state.setSelectedCell)
    const setCellValue = useSudokuStore((state) => state.setCellValue)

    const x = (col - 1) * width;
    const y = (row - 1) * width;

    const isSelected = selectedCell && row === selectedCell[0] && col === selectedCell[1];
    const fill = isSelected ? "red" : "white";

    const handleMouseDown = () => {
        selectCell([row, col]);
    }

    return (
        <g>
            <rect x={x} width={width} y={y} height={width} fill={fill} onMouseDown={handleMouseDown} />
            <text
                x={x + width / 2}
                y={y + width / 1.7}
                fontSize={100}
                color="black"
                dominantBaseline="middle"
                textAnchor="middle"
                pointerEvents="none"
            >
                {cellValue && cellValue[0]}
            </text>
        </g>
    );
};

export default Cell;