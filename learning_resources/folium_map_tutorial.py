"""
BI304: Folium Web Mapping Tutorial
Reference Video: https://www.youtube.com/watch?v=X8CoVymMOLw
Course: BI304 Empowering Data Through Storytelling and Visualization, TBS
Topic: Thammasat University Multi-Campus Network Mapping
"""

import folium
from folium.plugins import MiniMap, MarkerCluster

def create_thammasat_map(output_file="thammasat_campuses_map.html"):
    # Center map on Central Thailand
    tu_center = [14.0736, 100.6067] # Rangsit Campus center
    
    # Use CartoDB Positron tile layer to avoid OpenStreetMap rate-limit/403 block as taught in class
    m = folium.Map(
        location=[13.8, 100.5],
        zoom_start=7,
        tiles="CartoDB positron",
        control_scale=True
    )

    # Campus Data with coordinates, founding year, area, and student capacity
    campuses = [
        {
            "name": "Thammasat Tha Prachan (ท่าพระจันทร์)",
            "lat": 13.7557,
            "lng": 100.4930,
            "year": 1934,
            "area_rai": 49,
            "students": "6,500 (Graduate & International)",
            "role": "The Historic & Democratic Sanctuary / International Hub",
            "color": "#c62828",
            "icon": "university"
        },
        {
            "name": "Thammasat Rangsit Center (ศูนย์รังสิต)",
            "lat": 14.0736,
            "lng": 100.6067,
            "year": 1986,
            "area_rai": 1757,
            "students": "32,000 (Main Undergraduate & Research)",
            "role": "Smart & Green Mega-Campus / Medical Hub / Puey Centenary Park",
            "color": "#f57c00",
            "icon": "leaf"
        },
        {
            "name": "Thammasat Lampang Center (ศูนย์ลำปาง)",
            "lat": 18.2982,
            "lng": 99.4897,
            "year": 1996,
            "area_rai": 464,
            "students": "2,200",
            "role": "Northern Regional Education & Cultural Heritage Hub",
            "color": "#2e7d32",
            "icon": "mountain"
        },
        {
            "name": "Thammasat Pattaya Center (ศูนย์พัทยา)",
            "lat": 12.9236,
            "lng": 100.9925,
            "year": 1995,
            "area_rai": 566,
            "students": "1,500",
            "role": "Eastern Economic Corridor (EEC) / Automotive & High-Tech Hub",
            "color": "#1565c0",
            "icon": "car"
        }
    ]

    # Add markers with informative popups
    for c in campuses:
        popup_html = f"""
        <div style="font-family: 'Segoe UI', Tahoma, sans-serif; width: 260px; padding: 4px;">
            <h4 style="margin: 0 0 6px 0; color: #c62828; font-size: 15px; border-bottom: 2px solid #f9a825; padding-bottom: 4px;">
                {c['name']}
            </h4>
            <p style="margin: 4px 0; font-size: 13px;"><b>Founded:</b> B.E. {c['year'] + 543} (A.D. {c['year']})</p>
            <p style="margin: 4px 0; font-size: 13px;"><b>Land Area:</b> {c['area_rai']} Rai</p>
            <p style="margin: 4px 0; font-size: 13px;"><b>Student Body:</b> {c['students']}</p>
            <p style="margin: 4px 0; font-size: 12px; color: #555; background: #fdf5e6; padding: 4px 6px; border-radius: 4px;">
                {c['role']}
            </p>
        </div>
        """
        
        folium.Marker(
            location=[c["lat"], c["lng"]],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=c["name"],
            icon=folium.Icon(color="red" if c["year"]==1934 else "orange", icon="graduation-cap", prefix="fa")
        ).add_to(m)

        # Visual influence circle
        folium.Circle(
            location=[c["lat"], c["lng"]],
            radius=c["area_rai"] * 12,
            color=c["color"],
            weight=2,
            fill=True,
            fill_opacity=0.25,
            tooltip=f"{c['name']} Area: {c['area_rai']} Rai"
        ).add_to(m)

    # Connect Tha Prachan and Rangsit with a connection line (Migration corridor)
    folium.PolyLine(
        locations=[[13.7557, 100.4930], [14.0736, 100.6067]],
        color="#c62828",
        weight=3,
        dash_array="5, 10",
        tooltip="Strategic Campus Migration Corridor (42 km)"
    ).add_to(m)

    MiniMap(toggle_display=True).add_to(m)
    m.save(output_file)
    print(f"Map successfully generated and saved to {output_file}")

if __name__ == "__main__":
    create_thammasat_map()
