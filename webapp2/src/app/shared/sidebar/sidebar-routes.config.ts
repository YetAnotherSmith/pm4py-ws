import { RouteInfo } from './sidebar.metadata';

//Sidebar menu Routes and data
export const ROUTES: RouteInfo[] = [
    { path: '/real-ws/pmodel', title: 'Process Model', icon: 'ft-droplet', class: '', badge: '', badgeClass: '', isExternalLink: false, submenu: []},
    { path: '', title: 'Statistics', icon: 'ft-droplet', class: 'has-sub', badge: '', badgeClass: '', isExternalLink: false, submenu: [
            { path: '/real-ws/cases', title: 'Cases', icon: 'ft-droplet', class: '', badge: '', badgeClass: '', isExternalLink: false, submenu: []},
            { path: '/real-ws/statistics', title: 'Aggregated stats', icon: 'ft-droplet', class: '', badge: '', badgeClass: '', isExternalLink: false, submenu: []},
        ]
    },
];
