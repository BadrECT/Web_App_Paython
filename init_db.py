import os
import django
import sys

# Ajouter le répertoire parent au chemin Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')
django.setup()

from django.contrib.auth import get_user_model
from tasks.models import Project, Task

User = get_user_model()

def init_database():
    print("Initialisation de la base de données...")
    
    # Créer des utilisateurs de test
    try:
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'role': 'admin',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            print("✓ Admin user créé")

        manager, created = User.objects.get_or_create(
            username='manager',
            defaults={
                'email': 'manager@example.com',
                'role': 'manager',
                'first_name': 'John',
                'last_name': 'Manager'
            }
        )
        if created:
            manager.set_password('manager123')
            manager.save()
            print("✓ Manager user créé")

        user1, created = User.objects.get_or_create(
            username='user1',
            defaults={
                'email': 'user1@example.com',
                'role': 'user',
                'first_name': 'Alice',
                'last_name': 'Développeur'
            }
        )
        if created:
            user1.set_password('user1123')
            user1.save()
            print("✓ User1 créé")

        user2, created = User.objects.get_or_create(
            username='user2',
            defaults={
                'email': 'user2@example.com',
                'role': 'user',
                'first_name': 'Bob',
                'last_name': 'Designer'
            }
        )
        if created:
            user2.set_password('user2123')
            user2.save()
            print("✓ User2 créé")

        # Créer un projet de test
        project, created = Project.objects.get_or_create(
            name='Projet de Démonstration',
            defaults={
                'description': 'Ceci est un projet de démonstration pour tester le système de gestion de tâches. Ce projet inclut le développement d\'une application web complète avec Django.',
                'priority': 'high',
                'status': 'active',
                'manager': manager,
                'start_date': '2024-01-01',
                'end_date': '2024-12-31'
            }
        )
        if created:
            project.team_members.add(user1, user2)
            print("✓ Projet de démonstration créé")

        # Créer des tâches de test
        tasks_data = [
            {
                'title': 'Configurer l\'environnement de développement',
                'description': 'Installer et configurer tous les outils nécessaires au développement : Python, Django, MySQL, et les dépendances du projet.',
                'assigned_to': user1,
                'priority': 'high',
                'status': 'in_progress',
                'due_date': '2024-02-01',
                'estimated_hours': 8
            },
            {
                'title': 'Créer les modèles de données',
                'description': 'Définir et implémenter les modèles Django pour les utilisateurs, projets, tâches, commentaires et suivi du temps.',
                'assigned_to': user1,
                'priority': 'high',
                'status': 'done',
                'due_date': '2024-01-15',
                'estimated_hours': 16
            },
            {
                'title': 'Développer l\'interface utilisateur',
                'description': 'Créer les templates HTML avec Bootstrap et les assets CSS/JS pour une interface responsive et moderne.',
                'assigned_to': user2,
                'priority': 'medium',
                'status': 'in_progress',
                'due_date': '2024-02-15',
                'estimated_hours': 24
            },
            {
                'title': 'Implémenter l\'authentification',
                'description': 'Développer le système de connexion, déconnexion et gestion des permissions basées sur les rôles.',
                'assigned_to': user1,
                'priority': 'high',
                'status': 'done',
                'due_date': '2024-01-20',
                'estimated_hours': 12
            },
            {
                'title': 'Tests et déploiement',
                'description': 'Effectuer les tests fonctionnels et déployer l\'application sur le serveur de production.',
                'assigned_to': user2,
                'priority': 'medium',
                'status': 'todo',
                'due_date': '2024-03-01',
                'estimated_hours': 20
            }
        ]

        tasks_created = 0
        for task_data in tasks_data:
            task, created = Task.objects.get_or_create(
                title=task_data['title'],
                project=project,
                defaults={
                    'description': task_data['description'],
                    'assigned_to': task_data['assigned_to'],
                    'priority': task_data['priority'],
                    'status': task_data['status'],
                    'due_date': task_data['due_date'],
                    'estimated_hours': task_data['estimated_hours'],
                    'created_by': manager
                }
            )
            if created:
                tasks_created += 1

        print(f"✓ {tasks_created} tâches de test créées")

        # Créer un deuxième projet
        project2, created = Project.objects.get_or_create(
            name='Site Web Corporate',
            defaults={
                'description': 'Développement du nouveau site web corporate avec système de gestion de contenu.',
                'priority': 'medium',
                'status': 'planning',
                'manager': manager,
                'start_date': '2024-03-01',
                'end_date': '2024-06-30'
            }
        )
        if created:
            project2.team_members.add(user2)
            print("✓ Deuxième projet créé")

        print("\n" + "="*50)
        print("BASE DE DONNÉES INITIALISÉE AVEC SUCCÈS!")
        print("="*50)
        print("\nComptes de test créés:")
        print("👑 Admin     - username: admin, password: admin123")
        print("👔 Manager   - username: manager, password: manager123")
        print("👤 Utilisateur 1 - username: user1, password: user1123")
        print("👤 Utilisateur 2 - username: user2, password: user2123")
        print("\nAccédez à l'application: http://127.0.0.1:8000")
        print("Interface d'admin: http://127.0.0.1:8000/admin")
        
    except Exception as e:
        print(f"❌ Erreur lors de l'initialisation: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    init_database()