import { create } from "zustand";
import { immer } from 'zustand/middleware/immer';

type SudokuState = {
    fixedGrid: (number | undefined)[][],
    userGrid: (number | undefined)[][],
    errorGrid: boolean[][],
    variantData: {},
    selectedCell: [number, number] | undefined,
}

type SudokuActions = {
    setSelectedCell: (selectedCell: [number, number] | undefined) => void,
    setCellValue: (row: number, col: number, value: number | undefined) => void,
    setError: (row: number, col: number, value: boolean) => void,
    clearErrors: () => void,
}

type SudokuSelector<T> = (state: SudokuState) => T

// Log every time state is changed
const log = (config: any) => (set: (arg0: any) => void, get: () => any, api: any) => config((args: any) => {
    console.log("  applying", args)
    set(args)
    console.log("  new state", get())
}, get, api)

export const useSudokuStore = create<SudokuState & SudokuActions>(log(immer<SudokuState & SudokuActions>((set) => ({
    fixedGrid: Array.from({ length: 11 }, () => Array.from({ length: 11 }, () => undefined)),
    userGrid: Array.from({ length: 11 }, () => Array.from({ length: 11 }, () => undefined)),
    errorGrid: Array.from({ length: 11 }, () => Array.from({ length: 11 }, () => false)),
    variantData: {},
    selectedCell: [3, 2],

    setSelectedCell: (selectedCell: [number, number] | undefined) => set((state) => {
        state.selectedCell = selectedCell;
    }),
    setCellValue: (row: number, col: number, value: number | undefined) => set((state) => {
        state.userGrid[row][col] = value;
    }),
    setError: (row: number, col: number, value: boolean) => set((state) => {
        state.errorGrid[row][col] = value;
    }),
    clearErrors: () => set((state) => {
        state.errorGrid = Array.from({ length: 11 }, () => Array.from({ length: 11 }, () => false));
    }),
}))));

enum CellValueState {
    Fixed = "fixed",
    User = "user",
    Error = "error",
}

export const selectCellValue = (row: number, col: number): SudokuSelector<[number, CellValueState] | undefined> => {
    return (state) => {
        const fixed = state.fixedGrid[row]?.[col];
        if (fixed !== undefined) {
            return [fixed, CellValueState.Fixed];
        }
        const user = state.userGrid[row]?.[col];
        if (user !== undefined) {
            return [user, CellValueState.User]
        }

        return undefined
    }
}