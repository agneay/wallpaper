fetch("wallpapers.json")
    .then(res => res.json())
    .then(data => {
        const container = document.getElementById("gallery");

        Object.entries(data).forEach(([category, images]) => {
            const section = document.createElement("section");

            const title = document.createElement("h2");
            title.textContent = category;
            section.appendChild(title);

            const grid = document.createElement("div");
            grid.className = "grid";

            images.forEach(img => {
                const image = document.createElement("img");
                image.src = `${category}/${encodeURIComponent(img)}`;
                image.loading = "lazy";
                grid.appendChild(image);
            });

            section.appendChild(grid);
            container.appendChild(section);
        });
    });
