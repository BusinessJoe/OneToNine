interface CellProps {
    width: number,
    row: number,
    col: number,
}

const Cell = (props: CellProps) => {
    const x = (props.col - 1) * props.width;
    const y = (props.row - 1) * props.width;
    return (
        <rect x={x} width={props.width} y={y} height={props.width} fill="white" />
    );
};

export default Cell;