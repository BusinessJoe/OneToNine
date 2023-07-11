"use client"

import { useSudokuStore } from "../zustand/store";

interface CellProps {
    width: number,
    row: number,
    col: number,
}

const Cell = (props: CellProps) => {
    const x = (props.col - 1) * props.width;
    const y = (props.row - 1) * props.width;
    const selectedCell = useSudokuStore((state) => state.selectedCell)
    const selectCell = useSudokuStore((state) => state.setSelectedCell)

    const isSelected = selectedCell && props.row === selectedCell[0] && props.col === selectedCell[1];
    const fill = isSelected ? "red" : "white";

    const handleMouseDown = () => {
        selectCell([props.row, props.col]);
    }

    return (
        <rect x={x} width={props.width} y={y} height={props.width} fill={fill} onMouseDown={handleMouseDown} />
    );
};

export default Cell;