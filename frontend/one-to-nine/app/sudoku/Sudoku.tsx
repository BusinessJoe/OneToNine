import React from "react";
import Box from "./Box";
import Cell from "./Cell";
import Line from "./Line";
import Validator from "./Validator";

const Sudoku = () => {
    const width = 1000;
    const borderOffset = width / 9;

    const lines: React.JSX.Element[] = [];
    for (let i = 1; i < 9; i++) {
        lines.push(
            <Line key={i} vertical={true} index={i} width={width} />
        )
        lines.push(
            <Line key={i} vertical={false} index={i} width={width} />
        )
    }

    const cells: React.JSX.Element[] = [];
    for (let row = 1; row <= 9; row++) {
        for (let col = 1; col <= 9; col++) {
            cells.push(
                <Cell key={`${row},${col}`} row={row} col={col} width={width / 9} />
            );
        }
    }

    return (
        <>
            <Validator />
            <svg viewBox={`${-borderOffset} ${-borderOffset} ${width + 2 * borderOffset} ${width + 2 * borderOffset}`} >
                {cells}
                {lines}
                <Box width={width} />
            </svg>
        </>
    )
};

export default Sudoku;