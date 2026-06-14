import re

with open('app/templates/public/activities/list.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix has_content bug
content = content.replace('{% set has_content = false %}', '{% set state = namespace(has_content=false) %}')
content = content.replace('{% set has_content = true %}', '{% set state.has_content = true %}')
content = content.replace('{% if not has_content %}', '{% if not state.has_content %}')

# 2. Change Category Header
cat_header_old = """            <div id="{{ category.slug }}" class="scroll-mt-24">
                <div class="flex items-center gap-4 mb-8 border-b border-gray-100 pb-4">
                    {% if category.image_url %}
                    <img src="{{ category.image_url }}" alt="{{ category.name }}" class="w-12 h-12 rounded-lg object-cover shadow-sm">
                    {% else %}
                    <div class="w-12 h-12 bg-primary-50 rounded-lg flex items-center justify-center text-primary-600">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/></svg>
                    </div>
                    {% endif %}
                    <div>
                        <h2 class="text-3xl font-serif font-bold text-gray-900">{{ category.name }}</h2>
                        {% if category.description %}
                        <p class="text-gray-500 mt-1">{{ category.description }}</p>
                        {% endif %}
                    </div>
                </div>"""

cat_header_new = """            <div id="{{ category.slug }}" class="scroll-mt-24 relative rounded-3xl overflow-hidden mb-8 p-8 sm:p-12">
                {% if category.image_url %}
                <div class="absolute inset-0">
                    <img src="{{ category.image_url }}" alt="{{ category.name }}" class="w-full h-full object-cover">
                    <div class="absolute inset-0 bg-gray-900/70 backdrop-blur-sm"></div>
                </div>
                {% else %}
                <div class="absolute inset-0 bg-gray-50 border border-gray-100"></div>
                {% endif %}
                <div class="relative z-10">
                    <div class="mb-10 border-b {% if category.image_url %}border-white/20{% else %}border-gray-200{% endif %} pb-6">
                        <h2 class="text-3xl sm:text-4xl font-serif font-bold {% if category.image_url %}text-white{% else %}text-gray-900{% endif %}">{{ category.name }}</h2>
                        {% if category.description %}
                        <p class="{% if category.image_url %}text-gray-300{% else %}text-gray-500{% endif %} mt-2 text-lg">{{ category.description }}</p>
                        {% endif %}
                    </div>"""
content = content.replace(cat_header_old, cat_header_new)

# Close the new div at the end of category loop
content = content.replace("""                    {% endfor %}
                </div>
            </div>
        {% endif %}
    {% endfor %}""", """                    {% endfor %}
                    </div>
                </div>
            </div>
        {% endif %}
    {% endfor %}""")

# Change Other Experiences header
other_old = """        <div id="general" class="scroll-mt-24">
            <div class="flex items-center gap-4 mb-8 border-b border-gray-100 pb-4">
                <div class="w-12 h-12 bg-gray-100 rounded-lg flex items-center justify-center text-gray-500">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zm10 0a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zm10 0a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
                </div>
                <div>
                    <h2 class="text-3xl font-serif font-bold text-gray-900">Other Experiences</h2>
                </div>
            </div>"""

other_new = """        <div id="general" class="scroll-mt-24 relative rounded-3xl overflow-hidden mb-8 p-8 sm:p-12">
            <div class="absolute inset-0 bg-gray-50 border border-gray-100"></div>
            <div class="relative z-10">
                <div class="mb-10 border-b border-gray-200 pb-6">
                    <h2 class="text-3xl sm:text-4xl font-serif font-bold text-gray-900">Other Experiences</h2>
                </div>"""
content = content.replace(other_old, other_new)

# Close Other Experiences div
content = content.replace("""                {% endfor %}
            </div>
        </div>
    {% endif %}""", """                {% endfor %}
                </div>
            </div>
        </div>
    {% endif %}""")


# 3. Change Card Text (in both loops)
card_text_old = """                        <!-- Content -->
                        <div class="absolute inset-0 p-6 flex flex-col justify-end text-white">
                            <span class="inline-block px-3 py-1 bg-white/20 backdrop-blur-md rounded-full text-xs font-semibold tracking-wider uppercase w-max mb-3 border border-white/20">{{ act.packages|length }} Packages</span>
                            <h3 class="text-2xl font-bold font-serif mb-2 leading-tight">{{ act.name }}</h3>
                            {% if act.description %}
                            <p class="text-sm text-gray-200 line-clamp-2 mb-4">{{ act.description }}</p>
                            {% endif %}
                            
                            <div class="flex items-center text-primary-300 text-sm font-semibold group-hover:text-white transition-colors">"""

card_text_new = """                        <!-- Content -->
                        <div class="absolute inset-0 p-6 flex flex-col justify-end text-white">
                            <h3 class="text-2xl font-bold font-serif mb-1 leading-tight">{{ act.name }}</h3>
                            <span class="inline-block text-gray-300 text-sm font-medium mb-4">{{ act.packages|length }} Packages Available</span>
                            
                            <div class="flex items-center text-primary-300 text-sm font-semibold group-hover:text-white transition-colors">"""

content = content.replace(card_text_old, card_text_new)

with open('app/templates/public/activities/list.html', 'w', encoding='utf-8') as f:
    f.write(content)
