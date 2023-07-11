import { create } from "zustand";

interface SudokuState {
    fixedValues: (number | undefined)[][],
    userValues: (number | undefined)[][],
    variantData: {},
    selectedCell: [number, number] | undefined,

    setSelectedCell: (selectedCell: [number, number] | undefined) => void,
}

export const useSudokuStore = create<SudokuState>((set) => ({
    fixedValues: Array(9).map(
        () => Array(9).map(() => undefined)
    ),
    userValues: Array(9).map(
        () => Array(9).map(() => undefined)
    ),
    variantData: {},
    selectedCell: [3, 2],
    setSelectedCell: (selectedCell: [number, number] | undefined) => set(() => ({ selectedCell: selectedCell }))
}));