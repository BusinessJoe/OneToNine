interface LineProps {
    vertical: boolean,
    index: number,
    width: number
}

const Line = (props: LineProps) => {
    const width = props.width;
    const thinWidth = 5;
    const thickWidth = 10;

    const strokeWidth = props.index % 3 === 0 ? thickWidth : thinWidth;

    const common = {
        stroke: "black",
        "stroke-width": strokeWidth,
    };

    if (props.vertical) {
        const x = props.index / 9 * width;
        return (
            <line x1={x} x2={x} y1={0} y2={width} {...common} />
        )
    } else {
        const y = props.index / 9 * width;
        return (
            <line y1={y} y2={y} x1={0} x2={width} {...common} />
        );
    }
};

export default Line;