export const constructQueryParams = (updatedData) => {
    return new URLSearchParams({
        id: updatedData.id,
        name: updatedData.name,
        category: updatedData.category,
        description: updatedData.description,
        price: updatedData.price,
        quantity: updatedData.quantity,
        manufacture: updatedData.manufacture,
    }).toString();
};

export const constructSearchParams = (params) => {
    return new URLSearchParams(params).toString();
};