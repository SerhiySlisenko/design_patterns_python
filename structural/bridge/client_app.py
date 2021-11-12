
from structural.bridge.abstractions import ShapeAbstraction, SquareAbstraction, TriangleAbstraction
from structural.bridge.impl import RendererImplementation, RasterRendererImplementation, VectorRendererImplementation


def main() -> None:
    """
    Client app
    """

    raster_impl: RendererImplementation = RasterRendererImplementation()
    abstraction: ShapeAbstraction = SquareAbstraction(raster_impl)
    print(abstraction)

    vector_impl: RendererImplementation = VectorRendererImplementation()
    abstraction: ShapeAbstraction = TriangleAbstraction(vector_impl)
    print(abstraction)

    abstraction: ShapeAbstraction = SquareAbstraction(vector_impl)
    print(abstraction)


if __name__ == '__main__':
    main()
